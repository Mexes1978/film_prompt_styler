# 🚀 GitHub Repository Setup Guide

## 📁 Repository Structure

```
comfyui-film-photography-node/
├── README.md                    # Main documentation (use README_GITHUB.md)
├── LICENSE                      # MIT License
├── film_prompt_styler.py       # Main node code
├── __init__.py                 # ComfyUI registration
├── .gitignore                  # Git ignore file
├── docs/                       # Documentation folder
│   ├── EQUIPMENT_GUIDE.md     # All 43 photographers with equipment
│   ├── EXAMPLES.md            # Usage examples with images
│   └── CONTRIBUTING.md        # How to contribute
└── examples/                   # Example workflows
    └── basic_workflow.json    # Basic ComfyUI workflow
```

---

## 📝 Step-by-Step GitHub Setup

### 1. Create Repository
```bash
# On GitHub: Create new repository
# Name: comfyui-film-photography-node
# Description: Film photography history education tool for ComfyUI
# Public repository
# Add MIT License
# Don't add README (we'll use our custom one)
```

### 2. Prepare Files Locally
```bash
# Create directory
mkdir comfyui-film-photography-node
cd comfyui-film-photography-node

# Copy essential files
# - film_prompt_styler.py
# - __init__.py
# - README_GITHUB.md (rename to README.md)
# - EQUIPMENT_GUIDE.md (put in docs/)

# Create .gitignore
cat > .gitignore << 'GITIGNORE'
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.DS_Store
.vscode/
.idea/
GITIGNORE
```

### 3. Initialize Git
```bash
git init
git add .
git commit -m "Initial commit: Film Photography History Node for ComfyUI"
```

### 4. Push to GitHub
```bash
git remote add origin https://github.com/YOURUSERNAME/comfyui-film-photography-node.git
git branch -M main
git push -u origin main
```

---

## 📸 Add Screenshots

### What to Screenshot:
1. **Node Interface** - Show all the dropdowns
2. **Simple Example** - Tri-X + 50mm lens
3. **Photographer Preset** - Daido Moriyama in action
4. **Complex Setup** - Multiple categories enabled
5. **Results Comparison** - Same prompt with different photographers

### Where to Add:
```
examples/
├── screenshots/
│   ├── node_interface.png
│   ├── simple_example.png
│   ├── daido_moriyama.png
│   ├── comparison.png
│   └── workflow.png
```

Update README.md image links:
```markdown
![Film Photography Node](examples/screenshots/node_interface.png)
```

---

## 🏷️ Create Release

### Version 1.0.0 - Initial Release

```bash
git tag -a v1.0.0 -m "Initial release: 43 photographers, 240+ options"
git push origin v1.0.0
```

On GitHub:
1. Go to Releases
2. Click "Create a new release"
3. Tag: v1.0.0
4. Title: "v1.0.0 - Initial Release"
5. Description:
```
## 🎉 Initial Release

Film Photography History Node for ComfyUI

### Features:
- 43 master photographers with historical equipment
- 30+ film stocks
- 35+ legendary lenses  
- 35+ lighting techniques
- 40+ photography genres
- 20+ photography eras
- 35+ technical processes

### Installation:
Download and extract to `ComfyUI/custom_nodes/`

See README for full documentation.
```

---

## 📢 Promotion Checklist

### Reddit Posts:
- [ ] r/comfyui - "Film Photography History Node - Not just filters, actual photo education"
- [ ] r/StableDiffusion - Focus on quality results
- [ ] r/analog (maybe) - "Using AI to understand film photography"

### Post Template:
```
# Film Photography History Node for ComfyUI

I built a node that teaches actual photography history while generating images.

Instead of generic "vintage film" filters, you get:
- 43 real photographers (Daido Moriyama's Ricoh GR, Ansel Adams' 8x10)
- Their actual equipment and techniques
- 180 years of photographic craft

[Insert your comparison images]

Not AI slop - actual photographic knowledge.

GitHub: [link]
```

### Twitter/X:
```
Built a ComfyUI node that's basically a photography school 📸

43 legendary photographers
Their actual cameras, lenses, film
180 years of photo history

From Ricoh GR street (Moriyama) to 8x10 landscapes (Adams)

[images]

github.com/yourname/repo
```

---

## 🎯 GitHub Topics to Add

Click "Add topics" on your GitHub repo and add:
- `comfyui`
- `comfyui-custom-nodes`
- `photography`
- `film-photography`
- `stable-diffusion`
- `ai-art`
- `image-generation`
- `photography-education`
- `historical-photography`

---

## ✅ Final Checklist

- [ ] Repository created on GitHub
- [ ] All files uploaded
- [ ] README.md looks good (preview on GitHub)
- [ ] Screenshots added
- [ ] License file present (MIT)
- [ ] .gitignore configured
- [ ] First release created (v1.0.0)
- [ ] Topics added to repo
- [ ] Test installation from GitHub works
- [ ] Reddit posts ready
- [ ] Example images prepared

---

## 🚀 You're Ready!

Your photography education tool is ready to share with the world!

**Remember**: You're not selling filters. You're teaching photography history. 📚📸
