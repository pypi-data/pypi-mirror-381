# CursorFlow

**Complete page intelligence for AI-driven development**

CursorFlow captures comprehensive data from web applications - DOM structure, CSS properties, network activity, console logs, and performance metrics - enabling AI agents like Cursor to make intelligent decisions about UI improvements and debugging.

## 🎯 What CursorFlow Does

**Data Collection, Not Analysis** - We gather structured data, AI makes the decisions.

### **📊 Complete Page Intelligence**
Every screenshot captures everything:
- **DOM**: All elements with exact CSS properties
- **Network**: All requests, responses, and timing
- **Console**: All logs, errors, and warnings  
- **Performance**: Load times, memory usage, metrics
- **Visual**: Screenshots and pixel-perfect comparisons

### **🔄 Rapid Iteration Support**
- **Mockup comparison** with pixel-level analysis
- **Hot reload integration** for instant CSS testing
- **Persistent sessions** that survive code changes
- **Universal framework support** (React, Vue, PHP, Perl, anything)

### **🤖 AI-First Design**
All data structured for AI consumption:
- Consistent JSON format across all features
- Element-level CSS properties for precise modifications
- Error correlation with timing data
- Performance insights with actionable metrics

## 🚀 Quick Start

```bash
# Install
pip install cursorflow

# Test any page - captures everything automatically
cursorflow test --base-url http://localhost:3000 --actions '[
  {"navigate": "/dashboard"},
  {"wait_for": "#main-content"},
  {"screenshot": "dashboard-loaded"}
]'

# Compare mockup to implementation
cursorflow compare-mockup https://mockup.com/design --base-url http://localhost:3000
```

## 💻 Usage Examples

### **Basic Testing**
```python
from cursorflow import CursorFlow

flow = CursorFlow(base_url="http://localhost:3000")

# Every screenshot includes complete page data
results = await flow.execute_and_collect([
    {"navigate": "/dashboard"},
    {"screenshot": "loaded"}  # Captures DOM, network, console, performance
])

# Access structured data for AI analysis
screenshot = results['artifacts']['screenshots'][0]
elements = screenshot['dom_analysis']['elements']  # All elements + CSS
network = screenshot['network_data']               # All requests + timing
console = screenshot['console_data']               # All logs + errors
```

### **Mockup Comparison**
```python
# Compare design to implementation with complete element data
results = await flow.compare_mockup_to_implementation(
    mockup_url="https://mockup.com/design",
    implementation_url="http://localhost:3000/dashboard"
)

# AI gets exact differences and CSS properties for every element
differences = results['layout_analysis']['element_differences']
```

### **CSS Iteration**
```python
# Test CSS changes with hot reload - no page refresh needed
css_changes = [
    {"name": "spacing", "css": ".container { gap: 2rem; }"},
    {"name": "colors", "css": ".button { background: blue; }"}
]

results = await flow.css_iteration_persistent(
    base_actions=[{"navigate": "/page"}],
    css_changes=css_changes
)
```

## 🔧 CLI Commands

```bash
# Test any page with custom actions
cursorflow test --base-url http://localhost:3000 --actions '[
  {"navigate": "/login"},
  {"fill": {"selector": "#username", "value": "test@example.com"}},
  {"fill": {"selector": "#password", "value": "password123"}},
  {"click": "#login-button"},
  {"wait_for": ".dashboard"},
  {"screenshot": "logged-in"}
]'

# Simple page test (just navigate and screenshot)
cursorflow test --base-url http://localhost:3000 --path "/dashboard"

# Compare mockup to implementation
cursorflow compare-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --viewports '[{"width": 1440, "height": 900, "name": "desktop"}]'

# Iterate on CSS improvements
cursorflow iterate-mockup https://mockup.com/design \
  --base-url http://localhost:3000 \
  --css-improvements '[
    {"name": "spacing", "css": ".container { gap: 2rem; }"},
    {"name": "colors", "css": ".button { background: blue; }"}
  ]'
```

## 🌐 Universal Framework Support

Works with any web technology:
- **Modern**: React, Vue, Angular, Next.js, Svelte
- **Traditional**: PHP, Django, Rails, Laravel
- **Legacy**: Perl, mod_perl, OpenSAS, Classic ASP
- **Any URL**: Local development, staging, production

## 📊 What AI Gets

### **Complete Element Data**
```json
{
  "tagName": "button",
  "textContent": "Save Changes",
  "boundingBox": {"x": 100, "y": 200, "width": 120, "height": 40},
  "computedStyles": {
    "backgroundColor": "rgb(0, 123, 255)",
    "fontSize": "14px",
    "padding": "8px 16px",
    "borderRadius": "4px"
  }
}
```

### **Network Activity**
```json
{
  "network_summary": {
    "total_requests": 23,
    "failed_requests": 2,
    "average_response_time": 145.5
  },
  "failed_requests": [
    {"url": "/api/data", "status": 404, "timing": 1250}
  ]
}
```

### **Console Intelligence**
```json
{
  "console_summary": {
    "error_count": 1,
    "warning_count": 2
  },
  "errors": [
    {"text": "Cannot read property 'id' of undefined", "location": "app.js:42"}
  ]
}
```

## 📚 Documentation

**[📖 Complete User Manual](docs/USER_MANUAL.md)** - Everything you need:
- Installation and setup
- All features and examples
- CLI commands and Python API
- Troubleshooting guide

## 🎯 Perfect for AI Development

CursorFlow is designed specifically for AI agents:
- **Complete data collection** - AI gets full context
- **Structured output** - Consistent JSON format
- **No analysis** - We collect, AI decides
- **Rapid iteration** - Fast feedback loops
- **Universal compatibility** - Works with any web app

## Installation

```bash
pip install cursorflow
```

Browser dependencies install automatically on first use.

---

**CursorFlow: The data collection engine that powers AI-driven web development.** 🚀