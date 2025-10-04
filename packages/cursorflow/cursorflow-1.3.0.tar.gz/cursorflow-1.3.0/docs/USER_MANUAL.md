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
cursorflow test my-component --base-url http://localhost:3000
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

### 1. Test Any Component
```bash
cursorflow test dashboard --base-url http://localhost:3000
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
# Test a component
cursorflow test component-name --base-url http://localhost:3000

# Test with custom actions
cursorflow test login --actions '[
  {"navigate": "/login"},
  {"fill": {"selector": "#username", "value": "test"}},
  {"click": "#submit"},
  {"screenshot": "result"}
]'
```

### **Mockup Comparison**
```bash
# Compare mockup to implementation
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000

# Test multiple viewports
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --viewports '[
    {"width": 1440, "height": 900, "name": "desktop"},
    {"width": 768, "height": 1024, "name": "tablet"}
  ]'
```

### **CSS Iteration**
```bash
# Iterate on CSS improvements
cursorflow iterate-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --css-improvements improvements.json
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
