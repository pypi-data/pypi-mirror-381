"""
Universal Browser Controller

Framework-agnostic browser automation using Playwright.
No framework adapters needed - pure universal operations.
"""

import asyncio
import time
from typing import Dict, List, Any, Optional
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
import logging
from pathlib import Path


class BrowserController:
    """
    Universal browser automation - works with any web technology
    
    Provides simple, declarative interface without framework complexity.
    """
    
    def __init__(self, base_url: str, config: Dict):
        """
        Initialize browser controller
        
        Args:
            base_url: Base URL for testing
            config: {
                "headless": True,
                "debug_mode": False, 
                "human_timeout": 30,
                "viewport": {"width": 1440, "height": 900}
            }
        """
        self.base_url = base_url
        self.config = config
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        
        # Event tracking
        self.console_logs = []
        self.network_requests = []
        self.performance_metrics = []
        
        self.logger = logging.getLogger(__name__)
        
        # Ensure artifacts directory exists
        Path("artifacts/screenshots").mkdir(parents=True, exist_ok=True)
        
    async def initialize(self):
        """Initialize browser with universal settings"""
        try:
            self.playwright = await async_playwright().start()
            
            # Browser configuration - works for any framework
            browser_config = {
                "headless": self.config.get("headless", True),
                "slow_mo": 0 if self.config.get("headless", True) else 100,
                "args": [
                    "--disable-web-security",
                    "--disable-features=VizDisplayCompositor",
                    "--disable-background-timer-throttling",
                    "--disable-backgrounding-occluded-windows",
                    "--disable-renderer-backgrounding"
                ]
            }
            
            self.browser = await self.playwright.chromium.launch(**browser_config)
            
            # Context configuration
            viewport = self.config.get("viewport", {"width": 1440, "height": 900})
            context_config = {
                "viewport": viewport,
                "ignore_https_errors": True,
                "record_video_dir": "artifacts/videos" if self.config.get("record_video") else None
            }
            
            self.context = await self.browser.new_context(**context_config)
            self.page = await self.context.new_page()
            
            # Set up universal event listeners
            await self._setup_event_listeners()
            
            if not self.config.get("headless", True):
                self.logger.info("🖥️  Browser launched in FOREGROUND mode - human can interact")
            else:
                self.logger.info("🤖 Browser launched in HEADLESS mode - automated only")
                
        except Exception as e:
            self.logger.error(f"Browser initialization failed: {e}")
            raise
    
    async def _setup_event_listeners(self):
        """Set up universal event listeners for any framework"""
        
        # Console events
        self.page.on("console", self._handle_console_message)
        
        # Network events  
        self.page.on("request", self._handle_request)
        self.page.on("response", self._handle_response)
        
        # Page events
        self.page.on("pageerror", self._handle_page_error)
        self.page.on("crash", self._handle_page_crash)
        
    def _handle_console_message(self, msg):
        """Handle console messages from any framework"""
        log_entry = {
            "timestamp": time.time(),
            "type": msg.type,
            "text": msg.text,
            "location": {
                "url": msg.location.get("url", "") if msg.location else "",
                "line": msg.location.get("lineNumber", 0) if msg.location else 0,
                "column": msg.location.get("columnNumber", 0) if msg.location else 0
            },
            "args": [str(arg) for arg in msg.args] if msg.args else [],
            "stack_trace": getattr(msg, 'stackTrace', None)
        }
        self.console_logs.append(log_entry)
        
        # Enhanced logging for better correlation
        if msg.type == "error":
            self.logger.error(f"Console Error: {msg.text} at {msg.location}")
        elif msg.type == "warning":
            self.logger.warning(f"Console Warning: {msg.text}")
        elif msg.type in ["log", "info"] and any(keyword in msg.text.lower() for keyword in ["error", "failed", "exception"]):
            # Catch application logs that indicate errors
            self.logger.warning(f"App Error Log: {msg.text}")
    
    def _handle_request(self, request):
        """Handle network requests - framework agnostic"""
        # Capture complete request data
        request_data = {
            "timestamp": time.time(),
            "type": "request",
            "url": request.url,
            "method": request.method,
            "headers": dict(request.headers),
            "resource_type": request.resource_type,  # document, xhr, fetch, etc.
            "is_navigation_request": request.is_navigation_request()
        }
        
        # Capture complete payload data for all request types
        if request.post_data:
            request_data["post_data"] = request.post_data
            request_data["post_data_size"] = len(request.post_data)
            
            # Try to parse JSON payloads for better debugging
            content_type = request.headers.get("content-type", "")
            if "application/json" in content_type:
                try:
                    import json
                    request_data["parsed_json"] = json.loads(request.post_data)
                except:
                    pass
            elif "application/x-www-form-urlencoded" in content_type:
                try:
                    from urllib.parse import parse_qs
                    request_data["parsed_form"] = parse_qs(request.post_data)
                except:
                    pass
        
        # Capture query parameters
        from urllib.parse import urlparse, parse_qs
        parsed_url = urlparse(request.url)
        if parsed_url.query:
            request_data["query_params"] = parse_qs(parsed_url.query)
            
        # Capture file uploads
        if "multipart/form-data" in request.headers.get("content-type", ""):
            request_data["has_file_upload"] = True
            # Note: Actual file content not captured for performance/privacy
            
        self.network_requests.append(request_data)
        
        # Enhanced logging for correlation
        if request.resource_type in ["xhr", "fetch"] or "/api/" in request.url:
            payload_info = ""
            if request.post_data:
                payload_info = f" (payload: {len(request.post_data)} bytes)"
            self.logger.debug(f"API Request: {request.method} {request.url}{payload_info}")
            
            # Log critical data for immediate debugging
            if request.post_data and len(request.post_data) < 500:  # Only log small payloads
                self.logger.debug(f"Request payload: {request.post_data}")
    
    def _handle_response(self, response):
        """Handle network responses - framework agnostic"""
        response_data = {
            "timestamp": time.time(),
            "type": "response", 
            "url": response.url,
            "status": response.status,
            "status_text": response.status_text,
            "headers": dict(response.headers),
            "size": len(response.body) if hasattr(response, 'body') else 0,
            "from_cache": response.from_service_worker or False
        }
        self.network_requests.append(response_data)
        
        # Log failed requests for correlation
        if response.status >= 400:
            self.logger.warning(f"Failed Response: {response.status} {response.url}")
        
        # Capture response body for important requests
        should_capture_body = (
            response.status >= 400 or  # All error responses
            any(api_path in response.url for api_path in ["/api/", "/ajax", ".json"]) or  # API calls
            "application/json" in response.headers.get("content-type", "")  # JSON responses
        )
        
        if should_capture_body:
            asyncio.create_task(self._capture_response_body(response))
    
    def _handle_page_error(self, error):
        """Handle page errors from any framework"""
        self.console_logs.append({
            "timestamp": time.time(),
            "type": "pageerror",
            "text": str(error),
            "location": None
        })
        self.logger.error(f"Page error: {error}")
    
    def _handle_page_crash(self, page):
        """Handle page crashes"""
        self.logger.error("Page crashed - attempting recovery")
    
    async def navigate(self, path: str, wait_for_load: bool = True):
        """Navigate to URL - works with any web framework"""
        try:
            # Build full URL
            if path.startswith(("http://", "https://")):
                url = path
            else:
                url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
            
            self.logger.info(f"Navigating to: {url}")
            
            # Navigate and wait
            if wait_for_load:
                await self.page.goto(url, wait_until="networkidle", timeout=30000)
            else:
                await self.page.goto(url, timeout=30000)
                
            # Universal ready state check (works for any framework)
            await self.page.wait_for_load_state("domcontentloaded")
            
        except Exception as e:
            self.logger.error(f"Navigation failed to {path}: {e}")
            raise
    
    async def click(self, selector: str, timeout: int = 10000):
        """Click element - universal across frameworks"""
        try:
            await self.page.wait_for_selector(selector, timeout=timeout)
            await self.page.click(selector)
            self.logger.debug(f"Clicked: {selector}")
            
        except Exception as e:
            if not self.config.get("headless", True):
                # In foreground mode, allow human intervention
                self.logger.warning(f"Click failed for {selector}: {e}")
                self.logger.info(f"Human has {self.config.get('human_timeout', 30)} seconds to manually click...")
                await asyncio.sleep(self.config.get('human_timeout', 30))
            else:
                raise
    
    async def fill(self, selector: str, value: str, timeout: int = 10000):
        """Fill input field - universal"""
        try:
            await self.page.wait_for_selector(selector, timeout=timeout)
            await self.page.fill(selector, value)
            self.logger.debug(f"Filled {selector}: {value}")
            
        except Exception as e:
            self.logger.error(f"Fill failed for {selector}: {e}")
            raise
    
    async def type(self, selector: str, text: str, delay: int = 50):
        """Type text slowly - useful for complex forms"""
        try:
            await self.page.wait_for_selector(selector)
            await self.page.type(selector, text, delay=delay)
            self.logger.debug(f"Typed in {selector}: {text}")
            
        except Exception as e:
            self.logger.error(f"Type failed for {selector}: {e}")
            raise
    
    async def wait_for_element(self, selector: str, timeout: int = 30000, state: str = "visible"):
        """Wait for element - universal"""
        try:
            await self.page.wait_for_selector(selector, timeout=timeout, state=state)
            self.logger.debug(f"Element ready: {selector}")
            
        except Exception as e:
            self.logger.error(f"Wait failed for {selector}: {e}")
            raise
    
    async def wait_for_condition(self, condition: str, timeout: int = 30000):
        """Wait for custom JavaScript condition - universal"""
        try:
            await self.page.wait_for_function(condition, timeout=timeout)
            self.logger.debug(f"Condition met: {condition}")
            
        except Exception as e:
            self.logger.error(f"Condition wait failed: {condition}, {e}")
            raise
    
    async def screenshot(self, name: str, full_page: bool = False) -> str:
        """Take screenshot - universal"""
        try:
            timestamp = int(time.time())
            filename = f"artifacts/screenshots/{name}_{timestamp}.png"
            
            await self.page.screenshot(
                path=filename,
                full_page=full_page
            )
            
            self.logger.debug(f"Screenshot saved: {filename}")
            return filename
            
        except Exception as e:
            self.logger.error(f"Screenshot failed: {e}")
            raise
    
    async def evaluate_javascript(self, script: str) -> Any:
        """Execute JavaScript - universal"""
        try:
            result = await self.page.evaluate(script)
            return result
            
        except Exception as e:
            self.logger.error(f"JavaScript evaluation failed: {e}")
            raise
    
    async def get_computed_styles(self, selector: str) -> Dict:
        """Get computed styles for element - universal"""
        try:
            script = f"""
                (selector) => {{
                    const el = document.querySelector(selector);
                    if (!el) return null;
                    const styles = window.getComputedStyle(el);
                    return {{
                        position: styles.position,
                        display: styles.display,
                        flexDirection: styles.flexDirection,
                        justifyContent: styles.justifyContent,
                        alignItems: styles.alignItems,
                        width: styles.width,
                        height: styles.height,
                        margin: styles.margin,
                        padding: styles.padding,
                        fontSize: styles.fontSize,
                        color: styles.color,
                        backgroundColor: styles.backgroundColor
                    }};
                }}
            """
            
            result = await self.page.evaluate(script, selector)
            return result or {}
            
        except Exception as e:
            self.logger.error(f"Get computed styles failed for {selector}: {e}")
            return {}
    
    async def inject_css(self, css: str) -> bool:
        """Inject CSS into page - universal"""
        try:
            await self.page.add_style_tag(content=css)
            await self.page.wait_for_timeout(100)  # Let CSS apply
            return True
            
        except Exception as e:
            self.logger.error(f"CSS injection failed: {e}")
            return False
    
    async def set_viewport(self, width: int, height: int):
        """Change viewport size - universal"""
        try:
            await self.page.set_viewport_size({"width": width, "height": height})
            await self.page.wait_for_timeout(200)  # Let layout stabilize
            
        except Exception as e:
            self.logger.error(f"Viewport change failed: {e}")
            raise
    
    async def get_performance_metrics(self) -> Dict:
        """Get page performance metrics - universal"""
        try:
            metrics = await self.page.evaluate("""
                () => {
                    const perf = performance.getEntriesByType('navigation')[0];
                    return {
                        loadTime: perf ? perf.loadEventEnd - perf.loadEventStart : 0,
                        domContentLoaded: perf ? perf.domContentLoadedEventEnd - perf.domContentLoadedEventStart : 0,
                        firstPaint: performance.getEntriesByType('paint').find(p => p.name === 'first-paint')?.startTime || 0,
                        largestContentfulPaint: performance.getEntriesByType('largest-contentful-paint')[0]?.startTime || 0
                    };
                }
            """)
            
            return metrics
            
        except Exception as e:
            self.logger.error(f"Performance metrics failed: {e}")
            return {}
    
    async def cleanup(self):
        """Clean up browser resources"""
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
                
            self.logger.info("Browser cleanup completed")
            
        except Exception as e:
            self.logger.error(f"Browser cleanup failed: {e}")
    
    async def _capture_response_body(self, response):
        """Capture response body for API calls and errors"""
        try:
            body = await response.body()
            decoded_body = body.decode('utf-8', errors='ignore')
            
            # Find and update the matching response entry
            for req in reversed(self.network_requests):
                if (req.get("type") == "response" and 
                    req.get("url") == response.url and
                    req.get("status") == response.status):
                    
                    # Store raw body (truncated for large responses)
                    req["body"] = decoded_body[:2000]  # Increased limit for debugging
                    req["body_size"] = len(decoded_body)
                    req["body_truncated"] = len(decoded_body) > 2000
                    
                    # Parse JSON responses for easier debugging
                    content_type = response.headers.get("content-type", "")
                    if "application/json" in content_type:
                        try:
                            import json
                            req["parsed_json"] = json.loads(decoded_body)
                        except:
                            req["json_parse_error"] = True
                    
                    # Log important error responses for immediate visibility
                    if response.status >= 400:
                        error_preview = decoded_body[:200].replace('\n', ' ')
                        self.logger.error(f"Error response body: {error_preview}")
                    
                    break
                    
        except Exception as e:
            self.logger.warning(f"Failed to capture response body: {e}")
    
    async def capture_network_har(self) -> Dict:
        """Capture full network activity as HAR format"""
        try:
            # Get all network requests in HAR-like format
            har_entries = []
            
            for req in self.network_requests:
                if req.get("type") == "request":
                    # Find matching response
                    response = None
                    for resp in self.network_requests:
                        if (resp.get("type") == "response" and 
                            resp.get("url") == req.get("url") and
                            resp.get("timestamp", 0) > req.get("timestamp", 0)):
                            response = resp
                            break
                    
                    har_entry = {
                        "request": {
                            "method": req.get("method"),
                            "url": req.get("url"),
                            "headers": req.get("headers", {}),
                            "postData": req.get("post_data"),
                            "timestamp": req.get("timestamp")
                        },
                        "response": response if response else {"status": 0},
                        "time": (response.get("timestamp", 0) - req.get("timestamp", 0)) * 1000  # ms
                    }
                    har_entries.append(har_entry)
            
            return {"entries": har_entries}
            
        except Exception as e:
            self.logger.error(f"HAR capture failed: {e}")
            return {"entries": []}
    
    def get_console_errors(self) -> List[Dict]:
        """Get only console errors for quick analysis"""
        return [log for log in self.console_logs if log.get("type") == "error"]
    
    def get_failed_requests(self) -> List[Dict]:
        """Get only failed network requests"""
        failed = []
        for req in self.network_requests:
            if (req.get("type") == "response" and 
                req.get("status", 0) >= 400):
                failed.append(req)
        return failed
    
    def get_collected_data(self) -> Dict:
        """Get all collected browser data"""
        return {
            "console_logs": self.console_logs,
            "network_requests": self.network_requests,
            "performance_metrics": self.performance_metrics,
            "console_errors": self.get_console_errors(),
            "failed_requests": self.get_failed_requests(),
            "summary": {
                "total_console_logs": len(self.console_logs),
                "total_errors": len(self.get_console_errors()),
                "total_requests": len([r for r in self.network_requests if r.get("type") == "request"]),
                "failed_requests": len(self.get_failed_requests())
            }
        }
