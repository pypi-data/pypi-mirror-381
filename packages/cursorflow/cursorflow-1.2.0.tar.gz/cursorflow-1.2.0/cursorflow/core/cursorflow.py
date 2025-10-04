"""
CursorFlow - Main API Class

Simple, fast data collection engine that enables Cursor to autonomously test UI 
and iterate on designs with immediate visual feedback.

Design Philosophy: Declarative Actions | Batch Execution | Universal Correlation
"""

import asyncio
import time
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path

from .browser_controller import BrowserController
from .log_collector import LogCollector  
from .event_correlator import EventCorrelator
from .auth_handler import AuthHandler
from .css_iterator import CSSIterator
from .cursor_integration import CursorIntegration
from .persistent_session import PersistentSession, get_session_manager


class CursorFlow:
    """
    Main CursorFlow interface - Simple data collection for Cursor analysis
    
    Usage:
        flow = CursorFlow("http://localhost:3000", {"source": "local", "paths": ["logs/app.log"]})
        
        # Test UI flow
        results = await flow.execute_and_collect([
            {"navigate": "/dashboard"},
            {"click": "#refresh"},
            {"screenshot": "refreshed"}
        ])
        
        # CSS iteration
        visual_results = await flow.css_iteration_session(
            base_actions=[{"navigate": "/page"}],
            css_changes=[{"name": "fix", "css": ".item { margin: 1rem; }"}]
        )
    """
    
    def __init__(
        self, 
        base_url: str, 
        log_config: Dict, 
        auth_config: Optional[Dict] = None,
        browser_config: Optional[Dict] = None
    ):
        """
        Initialize CursorFlow with environment configuration
        
        Args:
            base_url: "http://localhost:3000" or "https://staging.example.com"
            log_config: {"source": "ssh|local|docker", "host": "...", "paths": [...]}
            auth_config: {"method": "form", "username_selector": "#user", ...}
            browser_config: {"headless": True, "debug_mode": False}
        """
        self.base_url = base_url
        self.log_config = log_config
        self.auth_config = auth_config or {}
        self.browser_config = browser_config or {"headless": True}
        
        # Initialize core components
        self.browser = BrowserController(base_url, self.browser_config)
        self.log_collector = LogCollector(log_config)
        self.correlator = EventCorrelator()
        self.auth_handler = AuthHandler(auth_config) if auth_config else None
        self.css_iterator = CSSIterator()
        self.cursor_integration = CursorIntegration()
        
        # Session tracking
        self.session_id = None
        self.timeline = []
        self.artifacts = {"screenshots": [], "console_logs": [], "server_logs": []}
        
        # Persistent session support for hot reload
        self.persistent_session: Optional[PersistentSession] = None
        self.session_manager = get_session_manager()
        
        self.logger = logging.getLogger(__name__)
        
        # Check for updates on initialization (background task)
        self._check_for_updates_async()
        
    async def execute_and_collect(
        self, 
        actions: List[Dict], 
        session_options: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Execute UI actions and collect all correlated data
        
        Args:
            actions: [
                {"navigate": "/dashboard"},
                {"click": "#refresh-button"},
                {"screenshot": "after-click"}
            ]
            session_options: {
                "reuse_session": True,
                "save_session": True, 
                "fresh_session": False
            }
            
        Returns:
            {
                "success": bool,
                "session_id": str,
                "timeline": [{"time": timestamp, "type": "browser|server", "event": "...", ...}],
                "correlations": [{"browser_event": "...", "server_event": "...", "confidence": 0.95}],
                "artifacts": {
                    "screenshots": ["before.png", "after.png"],
                    "console_logs": [...],
                    "server_logs": [...]
                }
            }
        """
        session_options = session_options or {}
        start_time = time.time()
        
        try:
            # Initialize session
            await self._initialize_session(session_options)
            
            # Start monitoring
            await self.log_collector.start_monitoring()
            
            # Execute actions
            success = await self._execute_actions(actions)
            
            # Stop monitoring and collect data
            server_logs = await self.log_collector.stop_monitoring()
            
            # Organize timeline (NO analysis - just data organization)
            organized_timeline = self.correlator.organize_timeline(
                self.timeline, server_logs
            )
            summary = self.correlator.get_summary(organized_timeline)
            
            # Package results
            results = {
                "success": success,
                "session_id": self.session_id,
                "execution_time": time.time() - start_time,
                "timeline": organized_timeline,  # Organized chronological data
                "browser_events": self.timeline,  # Raw browser events
                "server_logs": server_logs,       # Raw server logs
                "summary": summary,               # Basic counts
                "artifacts": self.artifacts
            }
            
            self.logger.info(f"Test execution completed: {success}, timeline events: {len(organized_timeline)}")
            return results
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "timeline": self.timeline,
                "artifacts": self.artifacts
            }
        finally:
            await self._cleanup_session(session_options)
    
    async def css_iteration_session(
        self, 
        base_actions: List[Dict], 
        css_changes: List[Dict],
        viewport_configs: Optional[List[Dict]] = None
    ) -> Dict[str, Any]:
        """
        Rapid CSS iteration with visual feedback
        
        Args:
            base_actions: [
                {"navigate": "/page"},
                {"wait_for": "#main-content"},
                {"screenshot": "baseline"}
            ]
            css_changes: [
                {
                    "name": "flex-spacing-fix",
                    "css": ".container { display: flex; gap: 1rem; }",
                    "rationale": "Fix spacing between items"
                }
            ]
            viewport_configs: [
                {"width": 1440, "height": 900, "name": "desktop"},
                {"width": 768, "height": 1024, "name": "tablet"}
            ]
            
        Returns:
            {
                "baseline": {
                    "screenshot": "baseline.png",
                    "computed_styles": {...},
                    "layout_metrics": {...}
                },
                "iterations": [
                    {
                        "name": "flex-spacing-fix",
                        "screenshot": "iteration_1.png",
                        "diff_image": "diff_1.png", 
                        "layout_changes": [...],
                        "console_errors": [...],
                        "performance_impact": {...}
                    }
                ]
            }
        """
        try:
            # Initialize for CSS iteration
            await self.browser.initialize()
            
            # Execute base actions and capture baseline
            await self._execute_actions(base_actions)
            baseline = await self.css_iterator.capture_baseline(self.browser.page)
            
            # Iterate through CSS changes
            iterations = []
            for i, css_change in enumerate(css_changes):
                iteration_result = await self.css_iterator.apply_css_and_capture(
                    self.browser.page, css_change, baseline
                )
                iterations.append(iteration_result)
                
            # Test across viewports if specified
            if viewport_configs:
                for viewport in viewport_configs:
                    await self.browser.set_viewport(viewport["width"], viewport["height"])
                    viewport_baseline = await self.css_iterator.capture_baseline(self.browser.page)
                    
                    for css_change in css_changes:
                        viewport_iteration = await self.css_iterator.apply_css_and_capture(
                            self.browser.page, css_change, viewport_baseline, 
                            suffix=f"_{viewport['name']}"
                        )
                        iterations.append(viewport_iteration)
            
            # Create raw results
            raw_results = {
                "baseline": baseline,
                "iterations": iterations,
                "summary": {
                    "total_changes": len(css_changes),
                    "viewports_tested": len(viewport_configs) if viewport_configs else 1,
                    "recommended_iteration": self._recommend_best_iteration(iterations)
                }
            }
            
            # Format for Cursor with session management and actionable insights
            cursor_results = self.cursor_integration.format_css_iteration_results(
                raw_results=raw_results,
                session_id=self.session_id,
                project_context={
                    "framework": "auto-detected",  # Could be enhanced with real detection
                    "base_url": self.base_url,
                    "test_type": "css_iteration"
                }
            )
            
            return cursor_results
            
        except Exception as e:
            self.logger.error(f"CSS iteration failed: {e}")
            return {"success": False, "error": str(e)}
        finally:
            await self.browser.cleanup()
    
    async def css_iteration_persistent(
        self,
        base_actions: List[Dict],
        css_changes: List[Dict],
        session_options: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        CSS iteration using persistent sessions for hot reload environments
        
        Maintains browser state between iterations, taking advantage of hot reload
        capabilities for faster CSS iteration cycles.
        
        Args:
            base_actions: Initial actions to set up the page
            css_changes: List of CSS changes to test
            session_options: {
                "session_id": "optional-custom-id",
                "reuse_session": True,
                "hot_reload": True,
                "keep_session_alive": True
            }
            
        Returns:
            Enhanced results with session information and hot reload data
        """
        session_options = session_options or {}
        start_time = time.time()
        
        try:
            # Get or create persistent session
            session_id = session_options.get("session_id", f"css_session_{int(time.time())}")
            self.persistent_session = await self.session_manager.get_or_create_session(
                session_id=session_id,
                base_url=self.base_url,
                config={
                    **self.browser_config,
                    "hot_reload_enabled": session_options.get("hot_reload", True),
                    "keep_alive": session_options.get("keep_session_alive", True)
                }
            )
            
            # Initialize persistent session
            session_initialized = await self.persistent_session.initialize()
            if not session_initialized:
                return {"success": False, "error": "Failed to initialize persistent session"}
            
            # Execute base actions if this is a new session or explicitly requested
            if (not session_options.get("reuse_session", True) or 
                not self.persistent_session.baseline_captured):
                
                self.logger.info("Executing base actions for CSS iteration setup")
                await self._execute_persistent_actions(base_actions)
                self.persistent_session.baseline_captured = True
            
            # Capture baseline state
            baseline = await self._capture_persistent_baseline()
            
            # Perform CSS iterations with persistent session
            iterations = []
            
            for i, css_change in enumerate(css_changes):
                self.logger.info(f"Applying CSS iteration {i+1}/{len(css_changes)}: {css_change.get('name', 'unnamed')}")
                
                # Apply CSS using persistent session (with hot reload when available)
                iteration_result = await self.persistent_session.apply_css_persistent(
                    css=css_change.get("css", ""),
                    name=css_change.get("name", f"iteration_{i+1}"),
                    replace_previous=css_change.get("replace_previous", False)
                )
                
                # Enhance with CursorFlow iteration data
                if iteration_result.get("success"):
                    enhanced_result = await self._enhance_iteration_result(
                        iteration_result, css_change, baseline
                    )
                    iterations.append(enhanced_result)
                else:
                    iterations.append(iteration_result)
                
                # Small delay to let changes settle
                await asyncio.sleep(0.1)
            
            # Get session information
            session_info = await self.persistent_session.get_session_info()
            
            # Create results
            results = {
                "success": True,
                "session_id": session_id,
                "execution_time": time.time() - start_time,
                "baseline": baseline,
                "iterations": iterations,
                "session_info": session_info,
                "hot_reload_used": session_info.get("hot_reload_available", False),
                "total_iterations": len(iterations),
                "summary": {
                    "successful_iterations": len([i for i in iterations if i.get("success", False)]),
                    "failed_iterations": len([i for i in iterations if not i.get("success", True)]),
                    "hot_reload_available": session_info.get("hot_reload_available", False),
                    "session_reused": session_options.get("reuse_session", True),
                    "recommended_iteration": self._recommend_best_iteration(iterations)
                }
            }
            
            # Format for Cursor integration
            cursor_results = self.cursor_integration.format_persistent_css_results(
                results, 
                {"framework": "auto-detected", "hot_reload": True}
            )
            
            # Keep session alive if requested
            if not session_options.get("keep_session_alive", True):
                await self.persistent_session.cleanup(save_state=True)
                self.persistent_session = None
            
            return cursor_results
            
        except Exception as e:
            self.logger.error(f"Persistent CSS iteration failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "session_id": session_id if 'session_id' in locals() else None
            }
    
    async def _execute_persistent_actions(self, actions: List[Dict]) -> bool:
        """Execute actions using persistent session"""
        try:
            for action in actions:
                if "navigate" in action:
                    path = action["navigate"]
                    if isinstance(path, dict):
                        path = path["url"]
                    await self.persistent_session.navigate_persistent(path)
                    
                elif "wait_for" in action:
                    selector = action["wait_for"]
                    if isinstance(selector, dict):
                        selector = selector["selector"]
                    await self.persistent_session.browser.wait_for_element(selector)
                    
                elif "screenshot" in action:
                    name = action["screenshot"]
                    await self.persistent_session.browser.screenshot(name)
                    
                # Add other actions as needed
            return True
            
        except Exception as e:
            self.logger.error(f"Persistent action execution failed: {e}")
            return False
    
    async def _capture_persistent_baseline(self) -> Dict[str, Any]:
        """Capture baseline using persistent session"""
        if not self.persistent_session or not self.persistent_session.browser:
            return {}
        
        try:
            # Use CSS iterator for baseline capture
            baseline = await self.css_iterator.capture_baseline(self.persistent_session.browser.page)
            
            # Enhance with persistent session data
            session_state = await self.persistent_session._capture_session_state("baseline")
            baseline.update({
                "session_state": session_state,
                "hot_reload_detected": await self.persistent_session._check_hot_reload_capability(),
                "iteration_context": {
                    "session_id": self.persistent_session.session_id,
                    "previous_iterations": self.persistent_session.iteration_count
                }
            })
            
            return baseline
            
        except Exception as e:
            self.logger.error(f"Persistent baseline capture failed: {e}")
            return {"error": str(e)}
    
    async def _enhance_iteration_result(
        self, 
        iteration_result: Dict, 
        css_change: Dict, 
        baseline: Dict
    ) -> Dict[str, Any]:
        """Enhance iteration result with CursorFlow analysis data"""
        try:
            enhanced = iteration_result.copy()
            
            # Add CSS iterator analysis
            if self.persistent_session and self.persistent_session.browser:
                css_analysis = await self.css_iterator.apply_css_and_capture(
                    page=self.persistent_session.browser.page,
                    css_change=css_change,
                    baseline=baseline,
                    suffix="_persistent"
                )
                
                # Merge analysis data
                enhanced.update({
                    "css_analysis": css_analysis,
                    "visual_comparison": css_analysis.get("changes", {}),
                    "performance_impact": css_analysis.get("performance_metrics", {}),
                    "console_errors": css_analysis.get("console_errors", [])
                })
            
            # Add persistent session context
            enhanced.update({
                "iteration_method": iteration_result.get("method", "standard"),
                "hot_reload_used": iteration_result.get("method") == "hot_reload",
                "session_persistent": True
            })
            
            return enhanced
            
        except Exception as e:
            self.logger.error(f"Failed to enhance iteration result: {e}")
            return iteration_result
    
    async def get_persistent_session_info(self) -> Optional[Dict[str, Any]]:
        """Get information about current persistent session"""
        if self.persistent_session:
            return await self.persistent_session.get_session_info()
        return None
    
    async def cleanup_persistent_session(self, save_state: bool = True):
        """Clean up current persistent session"""
        if self.persistent_session:
            await self.persistent_session.cleanup(save_state=save_state)
            self.persistent_session = None
    
    async def _initialize_session(self, session_options: Dict):
        """Initialize browser and authentication session"""
        self.session_id = f"session_{int(time.time())}"
        
        # Initialize browser
        await self.browser.initialize()
        
        # Handle authentication
        if self.auth_handler and not session_options.get("skip_auth", False):
            await self.auth_handler.authenticate(
                self.browser.page, 
                session_options
            )
    
    async def _execute_actions(self, actions: List[Dict]) -> bool:
        """Execute list of declarative actions"""
        try:
            for action in actions:
                await self._execute_single_action(action)
            return True
        except Exception as e:
            self.logger.error(f"Action execution failed: {e}")
            return False
    
    async def _execute_single_action(self, action: Dict):
        """Execute a single declarative action and track it"""
        action_start = time.time()
        
        try:
            # Navigation actions
            if "navigate" in action:
                url = action["navigate"]
                if isinstance(url, dict):
                    url = url["url"]
                await self.browser.navigate(url)
                
            # Interaction actions
            elif "click" in action:
                selector = action["click"]
                if isinstance(selector, dict):
                    selector = selector["selector"]
                await self.browser.click(selector)
                
            elif "fill" in action:
                config = action["fill"]
                await self.browser.fill(config["selector"], config["value"])
                
            elif "type" in action:
                config = action["type"]
                await self.browser.type(config["selector"], config["text"])
                
            # Waiting actions
            elif "wait" in action:
                await asyncio.sleep(action["wait"])
                
            elif "wait_for" in action:
                selector = action["wait_for"]
                if isinstance(selector, dict):
                    selector = selector["selector"]
                await self.browser.wait_for_element(selector)
                
            # Capture actions
            elif "screenshot" in action:
                name = action["screenshot"]
                screenshot_path = await self.browser.screenshot(name)
                self.artifacts["screenshots"].append(screenshot_path)
                
            elif "authenticate" in action:
                if self.auth_handler:
                    await self.auth_handler.authenticate(self.browser.page, action["authenticate"])
                    
            # Record action in timeline
            self.timeline.append({
                "timestamp": action_start,
                "type": "browser",
                "event": list(action.keys())[0],
                "data": action,
                "duration": time.time() - action_start
            })
            
        except Exception as e:
            self.logger.error(f"Action failed: {action}, error: {e}")
            raise
    
    async def _cleanup_session(self, session_options: Dict):
        """Clean up browser session"""
        try:
            # Save session if requested
            if session_options.get("save_session", False) and self.auth_handler:
                await self.auth_handler.save_session(self.browser.page, self.session_id)
                
            # Cleanup browser
            await self.browser.cleanup()
            
        except Exception as e:
            self.logger.error(f"Session cleanup failed: {e}")
    
    def _recommend_best_iteration(self, iterations: List[Dict]) -> Optional[str]:
        """Recommend best CSS iteration based on metrics"""
        if not iterations:
            return None
            
        # Simple scoring based on lack of console errors and performance
        best_iteration = None
        best_score = -1
        
        for iteration in iterations:
            score = 0
            
            # Penalty for console errors
            if not iteration.get("console_errors", []):
                score += 50
                
            # Bonus for good performance
            perf = iteration.get("performance_impact", {})
            if perf.get("render_time", 1000) < 100:
                score += 30
                
            if score > best_score:
                best_score = score
                best_iteration = iteration.get("name")
                
        return best_iteration
    
    def _check_for_updates_async(self):
        """Check for updates in background (non-blocking)"""
        try:
            import asyncio
            from ..auto_updater import check_for_updates_on_startup
            
            # Try to run update check in background
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # Schedule as background task
                    loop.create_task(check_for_updates_on_startup(str(Path.cwd())))
                else:
                    # Create new loop for quick check
                    asyncio.run(check_for_updates_on_startup(str(Path.cwd())))
            except Exception:
                # If async fails, skip silently - updates not critical for operation
                pass
        except ImportError:
            # Auto-updater not available, skip silently
            pass
