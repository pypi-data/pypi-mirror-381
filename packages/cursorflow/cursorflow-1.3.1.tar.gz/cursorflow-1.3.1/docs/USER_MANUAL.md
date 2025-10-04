# CursorFlow User Manual

**Complete guide to AI-powered UI testing and CSS iteration**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Core Features](#core-features)
5. [CLI Commands](#cli-commands)
6. [Python API](#python-api)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### Install and Test in 2 Minutes

```bash
# Install
pip install cursorflow

# Test your app
cursorflow test --base-url http://localhost:3000 --path "/dashboard"
```

**That's it!** CursorFlow captures screenshots, DOM data, network activity, console logs, and performance metrics automatically.

---

## 📦 Installation

### Requirements
- Python 3.8+
- A web application running locally or remotely

### Install CursorFlow
```bash
pip install cursorflow
```

### Install Browser (automatic on first use)
```bash
playwright install chromium  # Optional - happens automatically
```

---

## 🎯 Basic Usage

### 1. Test Any Page
```bash
cursorflow test --base-url http://localhost:3000 --path "/dashboard"
```

### 2. Compare Design to Implementation
```bash
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000
```

### 3. Get Complete Page Data
Every test captures:
- **Visual**: Screenshots and visual diffs
- **DOM**: All elements with exact CSS properties
- **Network**: All requests, responses, and timing
- **Console**: All logs, errors, and warnings
- **Performance**: Load times, memory usage, metrics

---

## 🔧 Core Features

### **🔬 Comprehensive Data Capture**
Every screenshot includes complete page intelligence:

```python
# Every test gives you everything
results = await flow.execute_and_collect([
    {"navigate": "/dashboard"},
    {"screenshot": "loaded"}
])

# Access all data
screenshot = results['artifacts']['screenshots'][0]
dom_data = screenshot['dom_analysis']        # All elements + CSS
network_data = screenshot['network_data']    # All requests + timing
console_data = screenshot['console_data']    # All logs + errors
performance = screenshot['performance_data'] # Load times + metrics
```

### **🎨 Mockup Comparison**
Compare designs to implementation with pixel precision:

```python
# Compare mockup to your app
results = await flow.compare_mockup_to_implementation(
    mockup_url="https://mockup.com/design",
    implementation_url="http://localhost:3000/dashboard"
)

# Get visual differences and exact CSS data for every element
```

### **⚡ Hot Reload CSS Iteration**
Test CSS changes without losing page state:

```python
# Test multiple CSS changes rapidly
css_changes = [
    {"name": "spacing", "css": ".container { gap: 2rem; }"},
    {"name": "colors", "css": ".button { background: blue; }"}
]

results = await flow.css_iteration_persistent(
    base_actions=[{"navigate": "/page"}],
    css_changes=css_changes
)
```

### **🤖 AI-First Design**
All data is structured for AI analysis:
- Consistent JSON format
- Complete element information
- Actionable error correlation
- Performance insights

---

## 💻 CLI Commands

### **Basic Testing**
```bash
# Simple page test (navigate and screenshot)
cursorflow test --base-url http://localhost:3000 --path "/dashboard"

# Test with custom actions
cursorflow test --base-url http://localhost:3000 --actions '[
  {"navigate": "/login"},
  {"fill": {"selector": "#username", "value": "test@example.com"}},
  {"fill": {"selector": "#password", "value": "password123"}},
  {"click": "#login-button"},
  {"wait_for": ".dashboard"},
  {"screenshot": "logged-in"}
]'

# Test with all options
cursorflow test \
  --base-url http://localhost:3000 \
  --actions '[
    {"navigate": "/products"},
    {"wait_for": ".product-grid"},
    {"click": ".filter-button"},
    {"fill": {"selector": "#search", "value": "laptop"}},
    {"click": "#apply-filter"},
    {"wait": 2},
    {"screenshot": "filtered-products"}
  ]' \
  --output results.json \
  --verbose
```

### **Mockup Comparison**
```bash
# Basic mockup comparison
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000

# Compare with multiple viewports
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --viewports '[
    {"width": 1440, "height": 900, "name": "desktop"},
    {"width": 768, "height": 1024, "name": "tablet"},
    {"width": 375, "height": 667, "name": "mobile"}
  ]'

# Compare with custom actions on both mockup and implementation
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --mockup-actions '[
    {"navigate": "/"},
    {"click": "#menu-toggle"},
    {"screenshot": "menu-open"}
  ]' \
  --implementation-actions '[
    {"navigate": "/"},
    {"wait_for": "#main-nav"},
    {"click": "#menu-toggle"},
    {"wait": 1},
    {"screenshot": "menu-open"}
  ]' \
  --diff-threshold 0.1 \
  --output comparison-results.json
```

### **CSS Iteration**
```bash
# Basic CSS iteration
cursorflow iterate-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --css-improvements '[
    {"name": "spacing", "css": ".container { gap: 2rem; padding: 1.5rem; }"},
    {"name": "colors", "css": ".button { background: #007bff; color: white; }"}
  ]'

# CSS iteration with custom base actions
cursorflow iterate-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --base-actions '[
    {"navigate": "/dashboard"},
    {"wait_for": "#main-content"},
    {"screenshot": "baseline"}
  ]' \
  --css-improvements '[
    {"name": "improve-layout", "css": ".grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }"},
    {"name": "better-typography", "css": "h1 { font-size: 2.5rem; font-weight: 600; }"},
    {"name": "enhanced-buttons", "css": ".btn { border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }"}
  ]' \
  --diff-threshold 0.05 \
  --output iteration-results.json

# Load CSS improvements from file
cursorflow iterate-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --css-improvements @css-improvements.json
```

### **Complete CLI Options Reference**

#### **`cursorflow test` Options:**
```bash
cursorflow test [OPTIONS]

Required:
  --base-url TEXT          Base URL of the application to test

Optional:
  --path TEXT              Simple path to navigate to (e.g., "/dashboard")
  --actions TEXT           JSON array of actions to perform
  --output TEXT            Output file for results (default: prints to stdout)
  --verbose               Enable verbose logging
  --headless              Run browser in headless mode (default: true)
  --timeout INTEGER       Timeout in seconds for actions (default: 30)
```

#### **`cursorflow compare-mockup` Options:**
```bash
cursorflow compare-mockup MOCKUP_URL [OPTIONS]

Required:
  MOCKUP_URL              URL of the mockup/design to compare against
  --base-url TEXT         Base URL of the implementation

Optional:
  --mockup-actions TEXT   JSON array of actions for mockup
  --implementation-actions TEXT  JSON array of actions for implementation
  --viewports TEXT        JSON array of viewport configurations
  --diff-threshold FLOAT  Similarity threshold (0.0-1.0, default: 0.1)
  --output TEXT          Output file for comparison results
  --verbose              Enable verbose logging
```

#### **`cursorflow iterate-mockup` Options:**
```bash
cursorflow iterate-mockup MOCKUP_URL [OPTIONS]

Required:
  MOCKUP_URL              URL of the mockup/design to match
  --base-url TEXT         Base URL of the implementation

Optional:
  --base-actions TEXT     JSON array of base actions before CSS changes
  --css-improvements TEXT JSON array of CSS improvements to test
  --diff-threshold FLOAT  Similarity threshold (0.0-1.0, default: 0.05)
  --output TEXT          Output file for iteration results
  --verbose              Enable verbose logging
```

#### **Action Types Reference:**
```json
{"navigate": "/path"}                                    // Navigate to path
{"click": "#selector"}                                   // Click element
{"fill": {"selector": "#input", "value": "text"}}      // Fill input field
{"select": {"selector": "#dropdown", "value": "option"}} // Select dropdown option
{"wait": 2}                                             // Wait seconds
{"wait_for": "#selector"}                               // Wait for element
{"screenshot": "name"}                                  // Take screenshot
{"screenshot": "name", "full_page": true}              // Full page screenshot
```

---

## 🐍 Python API

### **Basic Usage**
```python
from cursorflow import CursorFlow

# Initialize
flow = CursorFlow(
    base_url="http://localhost:3000",
    log_config={'source': 'local', 'paths': ['logs/app.log']}
)

# Test component
results = await flow.execute_and_collect([
    {"navigate": "/dashboard"},
    {"wait_for": "#content"},
    {"screenshot": "loaded"},
    {"click": "#button"},
    {"screenshot": "after_click"}
])
```

### **Mockup Comparison**
```python
# Compare mockup to implementation
results = await flow.compare_mockup_to_implementation(
    mockup_url="https://mockup.com/design",
    implementation_url="http://localhost:3000/dashboard",
    viewports=[{"width": 1440, "height": 900, "name": "desktop"}]
)

# Access comparison data
visual_diff = results['visual_analysis']
element_differences = results['layout_analysis']['element_differences']
```

### **CSS Iteration**
```python
# Test CSS changes with hot reload
css_changes = [
    {
        "name": "improve-spacing",
        "css": ".container { gap: 2rem; padding: 1.5rem; }",
        "rationale": "Better visual hierarchy"
    }
]

results = await flow.css_iteration_persistent(
    base_actions=[{"navigate": "/dashboard"}],
    css_changes=css_changes,
    session_options={"hot_reload": True}
)
```

---

## 📚 Examples

### **React/Next.js App**
```python
# Test React component
flow = CursorFlow(base_url="http://localhost:3000")

results = await flow.execute_and_collect([
    {"navigate": "/user-dashboard"},
    {"wait_for": "[data-testid='dashboard-content']"},
    {"screenshot": "dashboard_loaded"},
    {"click": "[data-testid='refresh-button']"},
    {"wait": 2},
    {"screenshot": "after_refresh"}
])
```

### **Legacy Perl/OpenSAS App**
```python
# Test OpenSAS component
flow = CursorFlow(base_url="http://localhost:8080")

results = await flow.execute_and_collect([
    {"navigate": "/message_console.smpl?orderid=12345"},
    {"wait_for": "#message_list"},
    {"screenshot": "console_loaded"},
    {"click": "#send_message"},
    {"screenshot": "message_sent"}
])
```

### **Mockup Comparison Workflow**
```python
# Complete mockup matching workflow
results = await flow.compare_mockup_to_implementation(
    mockup_url="https://figma.com/mockup",
    implementation_url="http://localhost:3000/dashboard"
)

# Analyze differences
for difference in results['layout_analysis']['element_differences']:
    print(f"Element: {difference['element_selector']}")
    print(f"Issue: {difference['difference_type']}")
    print(f"Fix: {difference['suggested_css']}")
```

---

## 🔍 Available Actions

### **Navigation**
```json
{"navigate": "/path"}
{"navigate": "/path", "params": {"id": "123"}}
```

### **Interaction**
```json
{"click": "#button"}
{"fill": {"selector": "#input", "value": "text"}}
{"select": {"selector": "#dropdown", "value": "option"}}
```

### **Waiting**
```json
{"wait": 2}
{"wait_for": "#element"}
{"wait_for_condition": "element_visible", "selector": "#element"}
```

### **Capture**
```json
{"screenshot": "name"}
{"screenshot": "name", "full_page": true}
```

---

## 🛠️ Troubleshooting

### **Common Issues**

#### **"Command not found: cursorflow"**
```bash
# Make sure it's installed
pip install cursorflow

# Check installation
cursorflow --version
```

#### **"Browser not found"**
```bash
# Install browser dependencies
playwright install chromium
```

#### **"Connection refused"**
```bash
# Make sure your app is running
curl http://localhost:3000  # Should respond

# Check the correct port
cursorflow test component --base-url http://localhost:8080
```

#### **"No logs found"**
```bash
# Check log paths exist
ls logs/app.log

# Use different log source
cursorflow test component --logs local
```

### **Getting Help**

#### **Check Results**
All test results are saved in `.cursorflow/artifacts/` with:
- Screenshots (visual evidence)
- JSON data (complete page state)
- Timeline (what happened when)

#### **Debug Mode**
```bash
# Run with verbose output
cursorflow test component --base-url http://localhost:3000 --verbose
```

#### **Verify Installation**
```python
# Test basic functionality
import cursorflow
print("✅ CursorFlow installed correctly")
```

---

## 🎯 Key Concepts

### **Universal Framework Support**
CursorFlow works with any web technology:
- **Modern**: React, Vue, Angular, Next.js
- **Traditional**: PHP, Django, Rails
- **Legacy**: Perl, mod_perl, OpenSAS
- **Any URL**: Local, staging, production

### **Complete Data Capture**
Every screenshot captures:
- **DOM**: All elements with computed CSS properties
- **Network**: All HTTP requests and responses with timing
- **Console**: All JavaScript logs, errors, and warnings
- **Performance**: Page load times, memory usage, paint metrics
- **Visual**: Screenshots and pixel-perfect comparisons

### **AI-Ready Output**
All data is structured for AI analysis:
- Consistent JSON format across all features
- Element-level CSS properties for precise modifications
- Error correlation with confidence scoring
- Actionable recommendations based on data

---

**That's everything you need to know!** CursorFlow is designed to be simple: point it at your app, and it captures everything an AI needs to understand and improve your UI. 🚀
