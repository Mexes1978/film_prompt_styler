# 📸 Film Photography History Node for ComfyUI

A comprehensive photography history education tool for ComfyUI. Generate images with authentic film photography aesthetics using historically accurate equipment, techniques, and photographer styles.

**Not just filters - actual photography knowledge from 180 years of photographic history.**

![Film Photography Node](https://via.placeholder.com/800x400/1a1a1a/ffffff?text=Film+Photography+Node)
*Add your screenshot here*

---

## 🎯 What Makes This Different

Most "film look" nodes just add grain and call it vintage. This node teaches you **actual photography history**:

- ✅ **43 Master Photographers** - with their real cameras, lenses, and film
- ✅ **Historical Equipment** - Ricoh GR (Daido Moriyama), Leica M4 (Cartier-Bresson), 8x10 view cameras (Ansel Adams)
- ✅ **Authentic Techniques** - Push processing, cross-processing, zone system
- ✅ **Educational** - Learn what gear produced iconic photographs
- ✅ **180 Years Covered** - From 1840s daguerreotypes to contemporary digital

---

## ✨ Features

### 🎭 **43 Photographer Styles** (Complete Workflows)
Each includes their actual equipment and techniques:
- **Daido Moriyama** - Ricoh GR compact 28mm, Tri-X pushed to 1600, Tokyo Provoke era
- **Ansel Adams** - 8x10 view camera, zone system, f/64 sharpness
- **Nan Goldin** - 35mm snapshot, Kodachrome slides, on-camera flash
- **Henri Cartier-Bresson** - Leica rangefinder 35mm/50mm, natural light only
- And 39 more legendary photographers...

### 🎞️ **30+ Film Stocks**
- **B&W**: Tri-X 400, HP5 Plus, Delta 3200, T-Max 100
- **Color Negative**: Portra 400/160/800, Pro 400H, Ektar 100
- **Color Slide**: Velvia 50/100, Kodachrome 64, Ektachrome
- **Specialty**: Cinestill 800T, Lomography, Instant films

### 🔍 **35+ Legendary Lenses**
- **Nikon**: 28mm f/2.8, 50mm f/1.4, 85mm f/1.8, 105mm f/2.5
- **Canon**: EF 50mm f/1.2L, EF 85mm f/1.2L
- **Leica**: Summilux 50mm f/1.4, Summicron 35mm f/2, Noctilux f/0.95
- **Zeiss**: Planar 50mm/85mm, Distagon 35mm
- **Soviet**: Helios 44-2 (swirly bokeh!), Jupiter-8
- **Medium Format**: Hasselblad 80mm, Pentax 67 105mm

### 💡 **35+ Lighting Techniques**
- **Historical**: Magnesium flash (1880s), Hot lights studio (1920s-50s)
- **Studio**: Rembrandt, Butterfly, Split, Loop, Clamshell
- **Natural**: Window light, Golden hour, Blue hour
- **Cinematic**: Film noir, Practical lighting
- **Flash**: Direct, Bounce, Off-camera, Ring light

### 🎨 **40+ Photography Genres**
Documentary, War photography, Street, Fashion, Beauty, Landscape, Architectural, Still life, Macro, Fine art, Conceptual, Scientific, Wedding, Lifestyle

### 🕰️ **20+ Photography Eras**
1840s Daguerreian, Pictorialism, Photo-Secession, f/64 Group, FSA Documentary, Film Noir, Street Photography Golden Age, New Color Movement, Contemporary Fine Art

### ⚗️ **35+ Technical Processes**
Push processing (+1/+2/+3 stops), Cross-processing (E-6 in C-41), Bleach bypass, Redscale, Double exposure, Solarization, Experimental techniques

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Film Photography History"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Install
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-film-photography-node
# Or download and extract ZIP
cd comfyui-film-photography-node
# Restart ComfyUI
```

### Method 3: Direct File Copy
```bash
cd ComfyUI/custom_nodes/
mkdir film_prompt_styler
cd film_prompt_styler
# Copy film_prompt_styler.py and __init__.py here
# Restart ComfyUI
```

---

## 🚀 Quick Start

### Simple Analog Look (Default)
```
Enable Film: ✓
Enable Lens: ✓
Film: Kodak Tri-X 400
Lens: Nikkor 50mm f/1.4
```
Result: Classic B&W film grain with natural bokeh

### Photographer Preset (One-Click Authentic)
```
Enable Photographer: ✓
Photographer: Daido Moriyama Style
```
Result: Ricoh GR compact, Tri-X pushed to 1600, harsh grain, Tokyo street aesthetic

### Full Control (Mix Everything)
```
Enable: Film ✓ | Lens ✓ | Lighting ✓ | Genre ✓ | Era ✓
Film: Kodak Portra 400
Lens: Canon EF 85mm f/1.2L
Lighting: Golden Hour
Genre: Portrait
Era: Contemporary
```

---

## 📚 Usage Examples

### Example 1: Tokyo Street Photography
```
Photographer: Daido Moriyama Style
→ Output: "shot with Ricoh GR compact 28mm, Tri-X pushed to 1600, 
harsh contrast printing, handheld motion blur, high contrast grain, 
Tokyo streets, Provoke era"
```

### Example 2: Ansel Adams Landscape
```
Photographer: Ansel Adams Style
Film: Any B&W
→ Output: "8x10 view camera, zone system precision, f/64 sharpness, 
dramatic landscapes, perfect tonal range, American West"
```

### Example 3: 1970s New Color
```
Era: 1960s-1970s New Color Movement
Film: Kodak Ektar 100
Lens: 35mm wide angle
→ Output: "1970s color photography revolution, democratic photography,
everyday America elevated, color as subject"
```

### Example 4: Fashion Editorial
```
Genre: Fashion Photography
Lighting: High Key Lighting
Photographer: Helmut Newton Style
```

---

## 🎓 Educational Philosophy

### This is NOT just another filter pack.

**It's a photography school.**

Every option teaches you:
- What equipment produced iconic images
- Why photographers made specific choices  
- How techniques shaped aesthetics
- The connection between gear and vision

### From Generic to Specific:
❌ **Generic**: "vintage film look"
✅ **Specific**: "Daido Moriyama - Ricoh GR, Tri-X pushed to 1600, Tokyo Provoke era"

### Intentional Craft Over Random Artifacts:
- No fake damage effects
- No random vintage overlays
- Only deliberate artistic choices
- Everything has historical context

---

## 🔧 Node Parameters

### Enable Switches (Toggle Categories On/Off):
- `enable_film` (ON by default)
- `enable_lens` (ON by default)
- `enable_lighting` (OFF by default)
- `enable_genre` (OFF by default)
- `enable_era` (OFF by default)
- `enable_process` (OFF by default)
- `enable_photographer` (OFF by default)
- `enable_print` (OFF by default - experimental)

### Dropdowns (Select Specific Options):
- `photographer_style` - 43 photographers
- `film_stock` - 30+ films
- `lens` - 35+ lenses
- `lighting_style` - 35+ techniques
- `photography_genre` - 40+ genres
- `photography_era` - 20+ eras
- `technical_process` - 35+ processes
- `print_style` - 30+ prints (experimental)

### Settings:
- `style_strength` - subtle/moderate/strong
- `add_technical_details` - include characteristics
- `custom_suffix` - add your own text

---

## 🎨 Workflow Integration

### Basic Workflow:
```
Film Photography Node → styled_prompt → CLIP Text Encode → Model
```

### With Preview:
```
Film Photography Node → styled_prompt → Show Text (preview)
                                      ↓
                               CLIP Text Encode → Model
```

### Multiple Styles:
```
Prompt 1 → Film Node (Daido) → styled_prompt_1 ─┐
Prompt 2 → Film Node (Adams) → styled_prompt_2 ─┤→ Batch → CLIP
Prompt 3 → Film Node (Goldin) → styled_prompt_3 ┘
```

---

## 📖 Complete Photographer List

<details>
<summary><b>Click to see all 43 photographers</b></summary>

### Black & White Masters
Ansel Adams, Henri Cartier-Bresson, Diane Arbus, Irving Penn, Richard Avedon, Annie Leibovitz, Robert Mapplethorpe, Sebastião Salgado, Nan Goldin, Josef Koudelka, Mary Ellen Mark

### Color Photography  
William Eggleston, Stephen Shore, Saul Leiter, Steve McCurry, Alex Webb

### Fashion
Helmut Newton, Guy Bourdin, Peter Lindbergh, Jo Ann Callis, Rineke Dijkstra

### Documentary
Dorothea Lange, Walker Evans, W. Eugene Smith, James Nachtwey, Robert Capa

### Street Photography
Garry Winogrand, Joel Meyerowitz, Vivian Maier, Anders Petersen, Bruce Gilden, Martin Parr

### Contemporary
Cindy Sherman, Andreas Gursky, Gregory Crewdson, Alex Prager, Todd Hido, Kat Toronto, Jeff Wall

### Japanese
Daido Moriyama, Nobuyoshi Araki

### Modernist
Man Ray

### Landscape
Edward Weston, Minor White

</details>

---

## 🤝 Contributing

Found a photographer missing? Want to add more film stocks? PRs welcome!

### Adding a Photographer:
1. Research their actual equipment
2. Add to `PHOTOGRAPHER_STYLES` with format:
```python
"Photographer Name Style": {
    "description": "Photographer Name aesthetic",
    "characteristics": "style traits. Equipment: camera, film, lens, process"
}
```
3. Include historical context and why they chose that gear

---

## 📜 License

MIT License - Use freely, credit appreciated

---

## 🙏 Acknowledgments

- Inspired by 180 years of photographic masters
- Equipment details researched from photographic archives
- Built for the ComfyUI community
- Special thanks to all the photographers who shaped visual history

---

## 📬 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/repo/discussions)
- **Reddit**: [Post your results!](https://reddit.com/r/comfyui)

---

## 🌟 Star History

If this node helps you understand photography history while making images, consider giving it a star! ⭐

---

**From AI slop to photographic craft** 📸🎓

*Your Ricoh GR connects you directly to Daido Moriyama's Tokyo streets.
That's the power of understanding equipment history.*
