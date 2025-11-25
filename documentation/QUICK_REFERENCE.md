# Quick Reference Guide - Marketplace Design System

## 🎨 CSS Classes & Utilities

### Text Styling
```html
<!-- Gradient Text -->
<h1 class="text-gradient">Title with Gradient</h1>

<!-- Color Classes -->
<p class="text-muted">Muted text</p>
<p class="text-primary">Primary text</p>
<p class="text-success">Success text</p>
<p class="text-danger">Danger text</p>
```

### Shadows & Elevation
```html
<!-- Shadow Levels -->
<div class="shadow-lg">Large Shadow</div>
<div class="shadow-sm">Small Shadow</div>
<div class="shadow">Default Shadow</div>
```

### Card Components
```html
<!-- Enhanced Card -->
<div class="card shadow-lg">
    <div class="card-header bg-gradient text-white">
        <h5 class="mb-0"><i class="fas fa-icon"></i> Header</h5>
    </div>
    <div class="card-body">
        Content here
    </div>
</div>
```

### Buttons
```html
<!-- Primary Gradient Button -->
<button class="btn btn-primary btn-lg">
    <i class="fas fa-check"></i> Button Text
</button>

<!-- Outline Button -->
<button class="btn btn-outline-primary">Outline</button>

<!-- Size Variants -->
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary btn-lg">Large</button>
```

### Forms
```html
<!-- Large Input Field -->
<input type="text" class="form-control form-control-lg" placeholder="Placeholder">

<!-- Form Label with Icon -->
<label class="form-label">
    <i class="fas fa-icon"></i> Label Text
</label>

<!-- Select Dropdown -->
<select class="form-select">
    <option>Option 1</option>
</select>
```

### Badges
```html
<!-- Status Badges -->
<span class="badge bg-success">Active</span>
<span class="badge bg-danger">Inactive</span>
<span class="badge bg-warning">Pending</span>
<span class="badge bg-info">Info</span>
```

### Alerts
```html
<!-- Success Alert -->
<div class="alert alert-success">Success message</div>

<!-- Danger Alert -->
<div class="alert alert-danger">Error message</div>

<!-- Info Alert -->
<div class="alert alert-info border-0">Info message</div>
```

---

## 🎨 Colors & Gradients

### Primary Colors
```css
/* Main Gradient */
--gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Individual Colors */
--purple-light: #667eea;
--purple-dark: #764ba2;

/* Status Colors */
--success: #28a745;
--danger: #dc3545;
--warning: #ffc107;
--info: #17a2b8;
```

### Usage in CSS
```css
/* Gradient Background */
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Gradient Text */
.text-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Gradient Border */
.border-gradient {
    border: 2px solid;
    border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
}
```

---

## 📱 Responsive Breakpoints

### Bootstrap Breakpoints
```css
/* Extra Small: < 576px (Mobile) */
/* Small: >= 576px (Landscape Mobile) */
/* Medium: >= 768px (Tablet) */
/* Large: >= 992px (Desktop) */
/* Extra Large: >= 1200px (Large Desktop) */
```

### Usage Examples
```html
<!-- Hide on Small Screens -->
<div class="d-none d-md-block">Desktop only</div>

<!-- Show on Small Screens Only -->
<div class="d-md-none">Mobile only</div>

<!-- Responsive Grid -->
<div class="col-12 col-md-6 col-lg-4">Responsive column</div>

<!-- Responsive Text Alignment -->
<div class="text-center text-lg-start">Aligned text</div>
```

---

## 🎬 Animations & Transitions

### Hover Effects
```css
/* Card Hover */
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

/* Button Hover */
.btn:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

/* Image Hover */
.img-hover:hover {
    transform: scale(1.05);
    opacity: 0.9;
}
```

### Transition Classes
```html
<!-- Smooth Transition All Properties -->
<div class="transition-all">Content</div>

<!-- Smooth Fade -->
<div style="transition: opacity 0.3s ease;">Fade effect</div>

<!-- Smooth Slide -->
<div style="transition: transform 0.3s ease;">Slide effect</div>
```

---

## 🔤 Typography

### Heading Styles
```html
<!-- Main Heading -->
<h1 class="display-4 fw-bold mb-3">Main Title</h1>

<!-- Section Heading -->
<h2 class="text-gradient mb-4">Section Title</h2>

<!-- Subsection Heading -->
<h3 class="mb-3">Subsection</h3>

<!-- Small Heading -->
<h6 class="fw-bold mb-2">Label</h6>
```

### Text Styles
```html
<!-- Lead Text (Larger) -->
<p class="lead">Introduction paragraph</p>

<!-- Small Text -->
<small class="text-muted">Small text</small>

<!-- Bold Text -->
<strong>Bold important text</strong>

<!-- Muted Text -->
<p class="text-muted">Disabled or secondary text</p>
```

---

## 🎯 Layout Patterns

### Hero Section
```html
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    padding: 80px 40px; border-radius: 12px; color: white;">
    <h1 class="display-4 fw-bold mb-3">Welcome</h1>
    <p class="lead mb-4">Description</p>
    <a href="#" class="btn btn-light btn-lg">Action</a>
</div>
```

### Sticky Sidebar
```html
<div class="col-lg-4">
    <div class="sticky-top" style="top: 80px;">
        <div class="card shadow-lg">
            <!-- Content -->
        </div>
    </div>
</div>
```

### Grid Layout
```html
<div class="row">
    <div class="col-md-6 col-lg-4 mb-4">
        <div class="card h-100 shadow-sm transition-all">
            <!-- Card content -->
        </div>
    </div>
</div>
```

### Two Column Layout
```html
<div class="row">
    <!-- Main Content -->
    <div class="col-lg-8 mb-4">
        <!-- Primary content -->
    </div>
    
    <!-- Sidebar -->
    <div class="col-lg-4">
        <!-- Secondary content -->
    </div>
</div>
```

---

## 🔍 Icons (Font Awesome 6.4.0)

### Common Icons
```html
<!-- Navigation -->
<i class="fas fa-home"></i>        <!-- Home -->
<i class="fas fa-user"></i>        <!-- User -->
<i class="fas fa-shopping-cart"></i> <!-- Cart -->
<i class="fas fa-star"></i>        <!-- Star -->

<!-- Status -->
<i class="fas fa-check-circle"></i> <!-- Success -->
<i class="fas fa-times-circle"></i> <!-- Error -->
<i class="fas fa-exclamation-triangle"></i> <!-- Warning -->
<i class="fas fa-info-circle"></i>  <!-- Info -->

<!-- Actions -->
<i class="fas fa-edit"></i>        <!-- Edit -->
<i class="fas fa-trash"></i>       <!-- Delete -->
<i class="fas fa-search"></i>      <!-- Search -->
<i class="fas fa-filter"></i>      <!-- Filter -->

<!-- Business -->
<i class="fas fa-store"></i>       <!-- Store -->
<i class="fas fa-box"></i>         <!-- Box/Product -->
<i class="fas fa-receipt"></i>     <!-- Invoice -->
<i class="fas fa-credit-card"></i> <!-- Payment -->
```

---

## 📋 Form Examples

### Login Form
```html
<form method="post" novalidate>
    {% csrf_token %}
    <div class="mb-3">
        <label class="form-label"><i class="fas fa-user"></i> Username</label>
        <input type="text" class="form-control form-control-lg" required>
    </div>
    <div class="mb-3">
        <label class="form-label"><i class="fas fa-lock"></i> Password</label>
        <input type="password" class="form-control form-control-lg" required>
    </div>
    <button type="submit" class="btn btn-primary btn-lg w-100">
        <i class="fas fa-sign-in-alt"></i> Login
    </button>
</form>
```

### Product Form
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="mb-3">
        <label class="form-label"><i class="fas fa-tag"></i> Product Name</label>
        {{ form.title }}
    </div>
    <div class="mb-3">
        <label class="form-label"><i class="fas fa-image"></i> Image</label>
        {{ form.image }}
    </div>
    <button type="submit" class="btn btn-primary">Save</button>
</form>
```

---

## 🧪 Testing Checklist

### Visual Testing
- [ ] Gradients render correctly
- [ ] Shadows appear properly
- [ ] Icons display correctly
- [ ] Colors match design
- [ ] Typography is readable
- [ ] Spacing is consistent

### Functional Testing
- [ ] Forms submit properly
- [ ] Links work correctly
- [ ] Buttons trigger actions
- [ ] Validations work
- [ ] Errors display correctly
- [ ] Success messages appear

### Responsive Testing
- [ ] Mobile layout works (< 576px)
- [ ] Tablet layout works (576-768px)
- [ ] Desktop layout works (> 768px)
- [ ] Navigation responsive
- [ ] Images scale properly
- [ ] Text readable on all sizes

### Browser Testing
- [ ] Chrome desktop
- [ ] Firefox desktop
- [ ] Safari desktop
- [ ] Edge desktop
- [ ] Chrome mobile
- [ ] Safari mobile

---

## 🐛 Common Issues & Solutions

### Issue: Gradient Text Not Showing
```css
/* Solution: Add all prefixes */
.text-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### Issue: Icons Not Loading
```html
<!-- Solution: Ensure CDN link in base.html -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

### Issue: Sticky Sidebar Not Working
```css
/* Solution: Ensure top offset */
.sticky-top {
    top: 80px; /* Height of navbar + padding */
}
```

### Issue: Forms Not Styled
```html
<!-- Solution: Apply form-control class -->
<input type="text" class="form-control form-control-lg">
<select class="form-select">
```

---

## 📚 Resources

### Documentation
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Font Awesome: https://fontawesome.com/icons/
- Django Templates: https://docs.djangoproject.com/en/5.2/topics/templates/
- CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/

### Tools
- Color Picker: https://colorpicker.com/
- Gradient Generator: https://cssgradient.io/
- Icon Search: https://fontawesome.com/icons/
- Bootstrap Grid: https://getbootstrap.com/docs/5.0/layout/grid/

---

## ✅ Quick Checklist for New Templates

- [ ] Extend base.html
- [ ] Add gradient text headings
- [ ] Use shadow-lg for cards
- [ ] Add icons throughout
- [ ] Apply form-control-lg to inputs
- [ ] Use status badges for states
- [ ] Add hover effects
- [ ] Test on mobile
- [ ] Verify icons load
- [ ] Check color contrast

---

## 💡 Pro Tips

1. **Reuse Classes**: Use utility classes instead of custom CSS
2. **Mobile First**: Design for mobile, then enhance for larger screens
3. **Consistent Spacing**: Use Bootstrap spacing utilities (p-3, m-3, etc.)
4. **Accessibility**: Always use proper semantic HTML and ARIA attributes
5. **Performance**: Avoid excessive animations and use GPU acceleration
6. **Testing**: Test on real devices, not just browsers
7. **Documentation**: Keep design decisions documented
8. **Consistency**: Follow the established design patterns

---

**Version**: 1.0
**Last Updated**: November 17, 2024
**Status**: ✅ Complete

