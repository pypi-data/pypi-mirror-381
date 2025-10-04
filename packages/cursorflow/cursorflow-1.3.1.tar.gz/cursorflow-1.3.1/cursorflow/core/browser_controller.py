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
    
    async def screenshot(self, name: str, full_page: bool = False, capture_comprehensive_data: bool = True) -> Dict[str, Any]:
        """Take screenshot with comprehensive page analysis - universal"""
        try:
            timestamp = int(time.time())
            screenshot_filename = f"artifacts/screenshots/{name}_{timestamp}.png"
            
            # Take the visual screenshot
            await self.page.screenshot(
                path=screenshot_filename,
                full_page=full_page
            )
            
            # Always return structured data for consistency
            screenshot_data = {
                "screenshot_path": screenshot_filename,
                "timestamp": timestamp,
                "name": name,
                "full_page": full_page
            }
            
            if capture_comprehensive_data:
                # Capture comprehensive page analysis
                comprehensive_data = await self._capture_comprehensive_page_analysis()
                
                # Save comprehensive data alongside screenshot
                data_filename = f"artifacts/screenshots/{name}_{timestamp}_comprehensive_data.json"
                import json
                with open(data_filename, 'w') as f:
                    json.dump(comprehensive_data, f, indent=2, default=str)
                
                # Merge all data into structured response
                screenshot_data.update({
                    "comprehensive_data_path": data_filename,
                    "dom_analysis": comprehensive_data.get("dom_analysis", {}),
                    "network_data": comprehensive_data.get("network_data", {}),
                    "console_data": comprehensive_data.get("console_data", {}),
                    "performance_data": comprehensive_data.get("performance_data", {}),
                    "page_state": comprehensive_data.get("page_state", {}),
                    "analysis_summary": comprehensive_data.get("analysis_summary", {})
                })
                
                self.logger.debug(f"Screenshot with comprehensive data saved: {screenshot_filename}, {data_filename}")
            else:
                self.logger.debug(f"Screenshot saved: {screenshot_filename}")
            
            return screenshot_data
            
        except Exception as e:
            self.logger.error(f"Screenshot with comprehensive analysis failed: {e}")
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
    
    async def _capture_comprehensive_page_analysis(self) -> Dict[str, Any]:
        """Capture comprehensive page analysis including DOM, network, console, and performance data"""
        try:
            # Capture DOM analysis
            dom_analysis = await self._capture_dom_analysis()
            
            # Capture current network state
            network_data = self._capture_network_data()
            
            # Capture current console state
            console_data = self._capture_console_data()
            
            # Capture performance metrics
            performance_data = await self._capture_performance_data()
            
            # Capture page state information
            page_state = await self._capture_page_state()
            
            # Create analysis summary
            analysis_summary = self._create_analysis_summary(dom_analysis, network_data, console_data, performance_data)
            
            return {
                "dom_analysis": dom_analysis,
                "network_data": network_data,
                "console_data": console_data,
                "performance_data": performance_data,
                "page_state": page_state,
                "analysis_summary": analysis_summary,
                "capture_timestamp": time.time(),
                "analysis_version": "2.0"
            }
            
        except Exception as e:
            self.logger.error(f"Comprehensive page analysis failed: {e}")
            return {"error": str(e), "capture_timestamp": time.time()}
    
    async def _capture_dom_analysis(self) -> Dict[str, Any]:
        """Capture comprehensive DOM structure and CSS data for every screenshot"""
        try:
            dom_analysis = await self.page.evaluate("""
                () => {
                    // Helper function to get element path
                    function getElementPath(element) {
                        const path = [];
                        while (element && element.nodeType === Node.ELEMENT_NODE) {
                            let selector = element.nodeName.toLowerCase();
                            if (element.id) {
                                selector += '#' + element.id;
                            } else if (element.className && typeof element.className === 'string') {
                                selector += '.' + element.className.split(' ').filter(c => c).join('.');
                            }
                            path.unshift(selector);
                            element = element.parentNode;
                        }
                        return path.join(' > ');
                    }
                    
                    // Helper function to get comprehensive computed styles
                    function getComputedStylesDetailed(element) {
                        const computed = window.getComputedStyle(element);
                        return {
                            // Layout properties
                            display: computed.display,
                            position: computed.position,
                            top: computed.top,
                            left: computed.left,
                            right: computed.right,
                            bottom: computed.bottom,
                            width: computed.width,
                            height: computed.height,
                            minWidth: computed.minWidth,
                            maxWidth: computed.maxWidth,
                            minHeight: computed.minHeight,
                            maxHeight: computed.maxHeight,
                            
                            // Flexbox properties
                            flexDirection: computed.flexDirection,
                            flexWrap: computed.flexWrap,
                            justifyContent: computed.justifyContent,
                            alignItems: computed.alignItems,
                            alignContent: computed.alignContent,
                            flex: computed.flex,
                            flexGrow: computed.flexGrow,
                            flexShrink: computed.flexShrink,
                            flexBasis: computed.flexBasis,
                            
                            // Grid properties
                            gridTemplateColumns: computed.gridTemplateColumns,
                            gridTemplateRows: computed.gridTemplateRows,
                            gridGap: computed.gridGap,
                            gridArea: computed.gridArea,
                            
                            // Spacing
                            margin: computed.margin,
                            marginTop: computed.marginTop,
                            marginRight: computed.marginRight,
                            marginBottom: computed.marginBottom,
                            marginLeft: computed.marginLeft,
                            padding: computed.padding,
                            paddingTop: computed.paddingTop,
                            paddingRight: computed.paddingRight,
                            paddingBottom: computed.paddingBottom,
                            paddingLeft: computed.paddingLeft,
                            
                            // Typography
                            fontFamily: computed.fontFamily,
                            fontSize: computed.fontSize,
                            fontWeight: computed.fontWeight,
                            fontStyle: computed.fontStyle,
                            lineHeight: computed.lineHeight,
                            letterSpacing: computed.letterSpacing,
                            textAlign: computed.textAlign,
                            textDecoration: computed.textDecoration,
                            textTransform: computed.textTransform,
                            
                            // Colors and backgrounds
                            color: computed.color,
                            backgroundColor: computed.backgroundColor,
                            backgroundImage: computed.backgroundImage,
                            backgroundSize: computed.backgroundSize,
                            backgroundPosition: computed.backgroundPosition,
                            backgroundRepeat: computed.backgroundRepeat,
                            
                            // Borders
                            border: computed.border,
                            borderTop: computed.borderTop,
                            borderRight: computed.borderRight,
                            borderBottom: computed.borderBottom,
                            borderLeft: computed.borderLeft,
                            borderRadius: computed.borderRadius,
                            borderWidth: computed.borderWidth,
                            borderStyle: computed.borderStyle,
                            borderColor: computed.borderColor,
                            
                            // Visual effects
                            boxShadow: computed.boxShadow,
                            opacity: computed.opacity,
                            transform: computed.transform,
                            transition: computed.transition,
                            animation: computed.animation,
                            
                            // Z-index and overflow
                            zIndex: computed.zIndex,
                            overflow: computed.overflow,
                            overflowX: computed.overflowX,
                            overflowY: computed.overflowY
                        };
                    }
                    
                    // Get all significant elements
                    const elements = [];
                    const selectors = [
                        // Structural elements
                        'body', 'main', 'header', 'nav', 'aside', 'footer', 'section', 'article',
                        // Common containers
                        '.container', '.wrapper', '.content', '.sidebar', '.header', '.footer',
                        '.navbar', '.nav', '.menu', '.main', '.page', '.app', '.layout',
                        // Interactive elements
                        'button', '.btn', '.button', 'a', '.link', 'input', 'form', '.form',
                        'select', 'textarea', '.input', '.field',
                        // Content elements
                        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', '.title', '.heading',
                        '.text', '.content', '.description',
                        // Layout elements
                        '.row', '.col', '.column', '.grid', '.flex', '.card', '.panel',
                        '.box', '.item', '.component',
                        // Common UI components
                        '.modal', '.dropdown', '.tooltip', '.alert', '.badge', '.tab',
                        '.table', '.list', '.menu-item'
                    ];
                    
                    selectors.forEach(selector => {
                        try {
                            document.querySelectorAll(selector).forEach((element, index) => {
                                const rect = element.getBoundingClientRect();
                                const computedStyles = getComputedStylesDetailed(element);
                                
                                // Only include visible elements with meaningful size
                                if (rect.width > 0 && rect.height > 0) {
                                    elements.push({
                                        selector: selector,
                                        index: index,
                                        uniqueSelector: selector + (index > 0 ? `:nth-of-type(${index + 1})` : ''),
                                        elementPath: getElementPath(element),
                                        tagName: element.tagName.toLowerCase(),
                                        id: element.id || null,
                                        className: element.className || null,
                                        textContent: element.textContent ? element.textContent.trim().substring(0, 200) : null,
                                        
                                        // Bounding box
                                        boundingBox: {
                                            x: Math.round(rect.x),
                                            y: Math.round(rect.y),
                                            width: Math.round(rect.width),
                                            height: Math.round(rect.height),
                                            top: Math.round(rect.top),
                                            left: Math.round(rect.left),
                                            right: Math.round(rect.right),
                                            bottom: Math.round(rect.bottom)
                                        },
                                        
                                        // All computed styles
                                        computedStyles: computedStyles,
                                        
                                        // Element attributes
                                        attributes: Array.from(element.attributes).reduce((attrs, attr) => {
                                            attrs[attr.name] = attr.value;
                                            return attrs;
                                        }, {}),
                                        
                                        // Element hierarchy info
                                        childrenCount: element.children.length,
                                        parentTagName: element.parentElement ? element.parentElement.tagName.toLowerCase() : null,
                                        
                                        // Visibility and interaction
                                        isVisible: rect.width > 0 && rect.height > 0 && 
                                                  computedStyles.display !== 'none' && 
                                                  computedStyles.visibility !== 'hidden' &&
                                                  parseFloat(computedStyles.opacity) > 0,
                                        isInteractive: ['button', 'a', 'input', 'select', 'textarea'].includes(element.tagName.toLowerCase()) ||
                                                      element.hasAttribute('onclick') ||
                                                      element.style.cursor === 'pointer'
                                    });
                                }
                            });
                        } catch (e) {
                            console.warn(`Failed to analyze selector ${selector}:`, e);
                        }
                    });
                    
                    // Get page-level information
                    const pageInfo = {
                        title: document.title,
                        url: window.location.href,
                        viewport: {
                            width: window.innerWidth,
                            height: window.innerHeight
                        },
                        documentSize: {
                            width: Math.max(
                                document.body.scrollWidth || 0,
                                document.body.offsetWidth || 0,
                                document.documentElement.clientWidth || 0,
                                document.documentElement.scrollWidth || 0,
                                document.documentElement.offsetWidth || 0
                            ),
                            height: Math.max(
                                document.body.scrollHeight || 0,
                                document.body.offsetHeight || 0,
                                document.documentElement.clientHeight || 0,
                                document.documentElement.scrollHeight || 0,
                                document.documentElement.offsetHeight || 0
                            )
                        },
                        scrollPosition: {
                            x: window.pageXOffset || document.documentElement.scrollLeft || 0,
                            y: window.pageYOffset || document.documentElement.scrollTop || 0
                        }
                    };
                    
                    // Analyze page structure
                    const pageStructure = {
                        hasHeader: elements.some(el => ['header', 'nav', '.header', '.navbar'].includes(el.selector)),
                        hasFooter: elements.some(el => ['footer', '.footer'].includes(el.selector)),
                        hasNavigation: elements.some(el => ['nav', '.nav', '.navbar', '.menu'].includes(el.selector)),
                        hasSidebar: elements.some(el => ['.sidebar', '.aside', 'aside'].includes(el.selector)),
                        hasMainContent: elements.some(el => ['main', '.main', '.content'].includes(el.selector)),
                        interactiveElements: elements.filter(el => el.isInteractive).length,
                        totalVisibleElements: elements.length
                    };
                    
                    return {
                        pageInfo: pageInfo,
                        pageStructure: pageStructure,
                        elements: elements,
                        totalElements: elements.length,
                        captureTimestamp: Date.now(),
                        analysisVersion: "1.0"
                    };
                }
            """)
            
            return dom_analysis
            
        except Exception as e:
            self.logger.error(f"DOM analysis failed: {e}")
            return {"error": str(e), "captureTimestamp": time.time()}
    
    def _capture_network_data(self) -> Dict[str, Any]:
        """Capture comprehensive network request and response data"""
        try:
            # Organize network requests by type
            requests = [req for req in self.network_requests if req.get("type") == "request"]
            responses = [req for req in self.network_requests if req.get("type") == "response"]
            
            # Categorize requests
            api_requests = [req for req in requests if any(api_path in req.get("url", "") for api_path in ["/api/", "/ajax", ".json", "/graphql"])]
            static_requests = [req for req in requests if req.get("resource_type") in ["stylesheet", "script", "image", "font"]]
            navigation_requests = [req for req in requests if req.get("is_navigation_request", False)]
            
            # Analyze failed requests
            failed_requests = [req for req in responses if req.get("status", 0) >= 400]
            
            # Calculate timing statistics
            request_timings = []
            for req in requests:
                # Find matching response
                matching_response = next((resp for resp in responses if resp.get("url") == req.get("url")), None)
                if matching_response:
                    timing = matching_response.get("timestamp", 0) - req.get("timestamp", 0)
                    request_timings.append({
                        "url": req.get("url"),
                        "method": req.get("method"),
                        "timing_ms": timing * 1000,
                        "status": matching_response.get("status"),
                        "size": matching_response.get("size", 0)
                    })
            
            return {
                "total_requests": len(requests),
                "total_responses": len(responses),
                "api_requests": {
                    "count": len(api_requests),
                    "requests": api_requests
                },
                "static_requests": {
                    "count": len(static_requests),
                    "requests": static_requests
                },
                "navigation_requests": {
                    "count": len(navigation_requests),
                    "requests": navigation_requests
                },
                "failed_requests": {
                    "count": len(failed_requests),
                    "requests": failed_requests
                },
                "request_timings": request_timings,
                "network_summary": {
                    "total_requests": len(requests),
                    "successful_requests": len([r for r in responses if 200 <= r.get("status", 0) < 400]),
                    "failed_requests": len(failed_requests),
                    "average_response_time": sum(t["timing_ms"] for t in request_timings) / len(request_timings) if request_timings else 0,
                    "total_data_transferred": sum(r.get("size", 0) for r in responses)
                },
                "all_network_events": self.network_requests  # Complete raw data
            }
            
        except Exception as e:
            self.logger.error(f"Network data capture failed: {e}")
            return {"error": str(e)}
    
    def _capture_console_data(self) -> Dict[str, Any]:
        """Capture comprehensive console log data"""
        try:
            # Categorize console logs
            errors = [log for log in self.console_logs if log.get("type") == "error"]
            warnings = [log for log in self.console_logs if log.get("type") == "warning"]
            info_logs = [log for log in self.console_logs if log.get("type") in ["log", "info"]]
            debug_logs = [log for log in self.console_logs if log.get("type") == "debug"]
            
            # Analyze error patterns
            error_patterns = {}
            for error in errors:
                error_text = error.get("text", "")
                # Group similar errors
                error_key = error_text[:100]  # First 100 chars as key
                if error_key not in error_patterns:
                    error_patterns[error_key] = {
                        "count": 0,
                        "first_occurrence": error.get("timestamp"),
                        "last_occurrence": error.get("timestamp"),
                        "sample_error": error
                    }
                error_patterns[error_key]["count"] += 1
                error_patterns[error_key]["last_occurrence"] = error.get("timestamp")
            
            # Recent activity (last 30 seconds)
            current_time = time.time()
            recent_logs = [log for log in self.console_logs if current_time - log.get("timestamp", 0) <= 30]
            
            return {
                "total_console_logs": len(self.console_logs),
                "errors": {
                    "count": len(errors),
                    "logs": errors,
                    "patterns": error_patterns
                },
                "warnings": {
                    "count": len(warnings),
                    "logs": warnings
                },
                "info_logs": {
                    "count": len(info_logs),
                    "logs": info_logs
                },
                "debug_logs": {
                    "count": len(debug_logs),
                    "logs": debug_logs
                },
                "recent_activity": {
                    "count": len(recent_logs),
                    "logs": recent_logs
                },
                "console_summary": {
                    "total_logs": len(self.console_logs),
                    "error_count": len(errors),
                    "warning_count": len(warnings),
                    "unique_error_patterns": len(error_patterns),
                    "has_recent_errors": any(log.get("type") == "error" for log in recent_logs)
                },
                "all_console_logs": self.console_logs  # Complete raw data
            }
            
        except Exception as e:
            self.logger.error(f"Console data capture failed: {e}")
            return {"error": str(e)}
    
    async def _capture_performance_data(self) -> Dict[str, Any]:
        """Capture comprehensive performance metrics"""
        try:
            # Get browser performance metrics
            browser_metrics = await self.get_performance_metrics()
            
            # Get additional performance data from the page
            additional_metrics = await self.page.evaluate("""
                () => {
                    const perf = performance;
                    const navigation = perf.getEntriesByType('navigation')[0];
                    const paint = perf.getEntriesByType('paint');
                    const resources = perf.getEntriesByType('resource');
                    
                    // Memory usage (if available)
                    const memory = performance.memory ? {
                        usedJSHeapSize: performance.memory.usedJSHeapSize,
                        totalJSHeapSize: performance.memory.totalJSHeapSize,
                        jsHeapSizeLimit: performance.memory.jsHeapSizeLimit
                    } : null;
                    
                    // Resource timing summary
                    const resourceSummary = {
                        totalResources: resources.length,
                        slowestResource: resources.reduce((slowest, resource) => 
                            resource.duration > (slowest?.duration || 0) ? resource : slowest, null),
                        averageLoadTime: resources.length > 0 ? 
                            resources.reduce((sum, r) => sum + r.duration, 0) / resources.length : 0
                    };
                    
                    return {
                        navigation: navigation ? {
                            domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
                            loadComplete: navigation.loadEventEnd - navigation.loadEventStart,
                            domInteractive: navigation.domInteractive - navigation.navigationStart,
                            domComplete: navigation.domComplete - navigation.navigationStart,
                            redirectTime: navigation.redirectEnd - navigation.redirectStart,
                            dnsTime: navigation.domainLookupEnd - navigation.domainLookupStart,
                            connectTime: navigation.connectEnd - navigation.connectStart,
                            requestTime: navigation.responseStart - navigation.requestStart,
                            responseTime: navigation.responseEnd - navigation.responseStart
                        } : null,
                        paint: {
                            firstPaint: paint.find(p => p.name === 'first-paint')?.startTime || 0,
                            firstContentfulPaint: paint.find(p => p.name === 'first-contentful-paint')?.startTime || 0
                        },
                        memory: memory,
                        resources: {
                            summary: resourceSummary,
                            details: resources.map(r => ({
                                name: r.name,
                                duration: r.duration,
                                size: r.transferSize,
                                type: r.initiatorType
                            }))
                        },
                        timing: {
                            now: performance.now(),
                            timeOrigin: performance.timeOrigin
                        }
                    };
                }
            """)
            
            return {
                "browser_metrics": browser_metrics,
                "detailed_metrics": additional_metrics,
                "performance_summary": {
                    "page_load_time": additional_metrics.get("navigation", {}).get("loadComplete", 0),
                    "dom_content_loaded": additional_metrics.get("navigation", {}).get("domContentLoaded", 0),
                    "first_paint": additional_metrics.get("paint", {}).get("firstPaint", 0),
                    "first_contentful_paint": additional_metrics.get("paint", {}).get("firstContentfulPaint", 0),
                    "total_resources": additional_metrics.get("resources", {}).get("summary", {}).get("totalResources", 0),
                    "memory_usage_mb": additional_metrics.get("memory", {}).get("usedJSHeapSize", 0) / (1024 * 1024) if additional_metrics.get("memory") else None
                }
            }
            
        except Exception as e:
            self.logger.error(f"Performance data capture failed: {e}")
            return {"error": str(e)}
    
    async def _capture_page_state(self) -> Dict[str, Any]:
        """Capture current page state information"""
        try:
            page_state = await self.page.evaluate("""
                () => {
                    return {
                        url: window.location.href,
                        title: document.title,
                        readyState: document.readyState,
                        visibilityState: document.visibilityState,
                        activeElement: document.activeElement ? {
                            tagName: document.activeElement.tagName,
                            id: document.activeElement.id,
                            className: document.activeElement.className
                        } : null,
                        viewport: {
                            width: window.innerWidth,
                            height: window.innerHeight,
                            scrollX: window.scrollX,
                            scrollY: window.scrollY
                        },
                        documentSize: {
                            width: Math.max(
                                document.body.scrollWidth || 0,
                                document.body.offsetWidth || 0,
                                document.documentElement.clientWidth || 0,
                                document.documentElement.scrollWidth || 0,
                                document.documentElement.offsetWidth || 0
                            ),
                            height: Math.max(
                                document.body.scrollHeight || 0,
                                document.body.offsetHeight || 0,
                                document.documentElement.clientHeight || 0,
                                document.documentElement.scrollHeight || 0,
                                document.documentElement.offsetHeight || 0
                            )
                        },
                        userAgent: navigator.userAgent,
                        timestamp: Date.now()
                    };
                }
            """)
            
            return page_state
            
        except Exception as e:
            self.logger.error(f"Page state capture failed: {e}")
            return {"error": str(e)}
    
    def _create_analysis_summary(self, dom_analysis: Dict, network_data: Dict, console_data: Dict, performance_data: Dict) -> Dict[str, Any]:
        """Create high-level analysis summary"""
        try:
            return {
                "page_health": {
                    "dom_elements_count": dom_analysis.get("totalElements", 0),
                    "has_errors": console_data.get("console_summary", {}).get("error_count", 0) > 0,
                    "error_count": console_data.get("console_summary", {}).get("error_count", 0),
                    "warning_count": console_data.get("console_summary", {}).get("warning_count", 0),
                    "failed_requests": network_data.get("network_summary", {}).get("failed_requests", 0),
                    "page_load_time_ms": performance_data.get("performance_summary", {}).get("page_load_time", 0)
                },
                "interaction_readiness": {
                    "interactive_elements": dom_analysis.get("pageStructure", {}).get("interactiveElements", 0),
                    "has_navigation": dom_analysis.get("pageStructure", {}).get("hasNavigation", False),
                    "has_main_content": dom_analysis.get("pageStructure", {}).get("hasMainContent", False),
                    "page_ready": dom_analysis.get("pageInfo", {}).get("title", "") != ""
                },
                "technical_metrics": {
                    "total_network_requests": network_data.get("network_summary", {}).get("total_requests", 0),
                    "average_response_time_ms": network_data.get("network_summary", {}).get("average_response_time", 0),
                    "memory_usage_mb": performance_data.get("performance_summary", {}).get("memory_usage_mb"),
                    "first_contentful_paint_ms": performance_data.get("performance_summary", {}).get("first_contentful_paint", 0)
                },
                "quality_indicators": {
                    "has_console_errors": console_data.get("console_summary", {}).get("has_recent_errors", False),
                    "has_failed_requests": network_data.get("failed_requests", {}).get("count", 0) > 0,
                    "performance_score": self._calculate_performance_score(performance_data),
                    "overall_health": "good" if (
                        console_data.get("console_summary", {}).get("error_count", 0) == 0 and
                        network_data.get("failed_requests", {}).get("count", 0) == 0 and
                        performance_data.get("performance_summary", {}).get("page_load_time", 0) < 3000
                    ) else "needs_attention"
                }
            }
            
        except Exception as e:
            self.logger.error(f"Analysis summary creation failed: {e}")
            return {"error": str(e)}
    
    def _calculate_performance_score(self, performance_data: Dict) -> int:
        """Calculate a simple performance score (0-100)"""
        try:
            score = 100
            
            # Deduct points for slow loading
            load_time = performance_data.get("performance_summary", {}).get("page_load_time", 0)
            if load_time > 3000:
                score -= 30
            elif load_time > 1000:
                score -= 15
            
            # Deduct points for slow first contentful paint
            fcp = performance_data.get("performance_summary", {}).get("first_contentful_paint", 0)
            if fcp > 2000:
                score -= 20
            elif fcp > 1000:
                score -= 10
            
            # Deduct points for high memory usage
            memory_mb = performance_data.get("performance_summary", {}).get("memory_usage_mb")
            if memory_mb and memory_mb > 100:
                score -= 20
            elif memory_mb and memory_mb > 50:
                score -= 10
            
            return max(0, score)
            
        except Exception as e:
            return 50  # Default middle score if calculation fails

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
