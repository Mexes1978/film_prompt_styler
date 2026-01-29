"""
ComfyUI Custom Node: Film Photography History Prompt Styler
Comprehensive photography history node covering film stocks, lenses, print processes, 
camera formats, and historical eras from the 1840s to present day.
A complete photography encyclopedia for AI image generation.
"""

class FilmPromptStyler:
    """
    A comprehensive ComfyUI node for authentic film photography aesthetics.
    
    Features:
    - 30+ classic film stocks (B&W, color negative, slide, instant, specialty)
    - 35+ legendary photography lenses (Nikon, Canon, Leica, Zeiss, vintage Soviet, medium format)
    - 35+ lighting techniques (historical, studio, natural, cinematic)
    - 40+ photography genres (documentary, fashion, landscape, scientific, fine art)
    - 30+ print styles and darkroom processes (silver gelatin, platinum, alternative processes, toning)
    - 20+ photography eras and movements (1840s-present, pictorialism, modernism, street photography)
    - 35+ technical processes (push/pull, cross-process, bleach bypass, experimental)
    - 43+ photographer styles (complete aesthetic signatures with historical equipment details)
    
    A complete photography history encyclopedia for AI models - focused on intentional artistic choices, not accidents.
    Every photographer includes their actual equipment: cameras, lenses, film, lighting, and printing methods.
    """
    
    # Lens definitions with their characteristics
    LENSES = {
        "None (Film Only)": {
            "description": "",
            "characteristics": ""
        },
        
        # Nikon F-Mount Lenses
        "Nikkor 50mm f/1.4": {
            "description": "shot with Nikkor 50mm f/1.4 lens",
            "characteristics": "creamy bokeh, sharp rendering, natural perspective, classic portrait lens, smooth out-of-focus areas"
        },
        "Nikkor 50mm f/1.8": {
            "description": "shot with Nikkor 50mm f/1.8 lens",
            "characteristics": "sharp center, slight field curvature, affordable classic look, neutral rendering"
        },
        "Nikkor 28mm f/2.8": {
            "description": "shot with Nikkor 28mm f/2.8 lens",
            "characteristics": "wide angle perspective, good sharpness, minimal distortion, street photography lens"
        },
        "Nikkor 35mm f/2": {
            "description": "shot with Nikkor 35mm f/2 lens",
            "characteristics": "documentary perspective, sharp across frame, natural field of view, photojournalism standard"
        },
        "Nikkor 85mm f/1.8": {
            "description": "shot with Nikkor 85mm f/1.8 lens",
            "characteristics": "beautiful bokeh, compressed perspective, flattering portraits, smooth background separation"
        },
        "Nikkor 105mm f/2.5": {
            "description": "shot with Nikkor 105mm f/2.5 lens",
            "characteristics": "classic portrait lens, excellent bokeh, high contrast, sharp rendering, legendary optics"
        },
        "Nikkor 135mm f/2.8": {
            "description": "shot with Nikkor 135mm f/2.8 lens",
            "characteristics": "strong compression, beautiful bokeh, isolates subject, dreamy out-of-focus rendering"
        },
        
        # Canon FD/EF Lenses
        "Canon FD 50mm f/1.4": {
            "description": "shot with Canon FD 50mm f/1.4 lens",
            "characteristics": "warm rendering, swirly bokeh, vintage character, classic 70s-80s aesthetic"
        },
        "Canon FD 85mm f/1.8": {
            "description": "shot with Canon FD 85mm f/1.8 lens",
            "characteristics": "smooth bokeh, soft rendering wide open, portrait specialty, vintage warmth"
        },
        "Canon EF 50mm f/1.2L": {
            "description": "shot with Canon EF 50mm f/1.2L lens",
            "characteristics": "ultra shallow depth of field, dreamy bokeh, soft focus wide open, ethereal rendering, professional portrait lens"
        },
        "Canon EF 85mm f/1.2L": {
            "description": "shot with Canon EF 85mm f/1.2L lens",
            "characteristics": "legendary bokeh, extremely shallow depth of field, dreamy rendering, professional portrait standard"
        },
        "Canon EF 35mm f/1.4L": {
            "description": "shot with Canon EF 35mm f/1.4L lens",
            "characteristics": "wide aperture, sharp rendering, photojournalism quality, natural perspective"
        },
        
        # Leica M-Mount Lenses
        "Leica Summilux 50mm f/1.4": {
            "description": "shot with Leica Summilux 50mm f/1.4 lens",
            "characteristics": "legendary optical quality, smooth bokeh, high contrast, micro contrast excellence, rangefinder aesthetic"
        },
        "Leica Summicron 35mm f/2": {
            "description": "shot with Leica Summicron 35mm f/2 lens",
            "characteristics": "exceptional sharpness, perfect rendering, street photography legend, rangefinder classic"
        },
        "Leica Noctilux 50mm f/0.95": {
            "description": "shot with Leica Noctilux 50mm f/0.95 lens",
            "characteristics": "extreme shallow depth of field, unique bokeh swirl, dreamy rendering, ultra-fast aperture, legendary mystique"
        },
        "Leica APO-Summicron 75mm f/2": {
            "description": "shot with Leica APO-Summicron 75mm f/2 lens",
            "characteristics": "perfect optical correction, clinical sharpness, neutral rendering, apochromatic quality"
        },
        
        # Zeiss Lenses
        "Zeiss Planar 50mm f/1.4": {
            "description": "shot with Zeiss Planar 50mm f/1.4 lens",
            "characteristics": "high contrast, excellent sharpness, clinical precision, Zeiss pop, neutral color"
        },
        "Zeiss Planar 85mm f/1.4": {
            "description": "shot with Zeiss Planar 85mm f/1.4 lens",
            "characteristics": "3D pop, high micro contrast, smooth bokeh, sharp rendering, professional portrait lens"
        },
        "Zeiss Distagon 35mm f/2": {
            "description": "shot with Zeiss Distagon 35mm f/2 lens",
            "characteristics": "controlled distortion, excellent edge-to-edge sharpness, wide angle precision"
        },
        "Zeiss Sonnar 135mm f/2.8": {
            "description": "shot with Zeiss Sonnar 135mm f/2.8 lens",
            "characteristics": "smooth bokeh, vintage character, portrait compression, classic optics"
        },
        
        # Vintage Soviet Lenses
        "Helios 44-2 58mm f/2": {
            "description": "shot with Helios 44-2 58mm f/2 lens",
            "characteristics": "swirly bokeh, vintage rendering, unique character, cult classic aesthetic, dreamy backgrounds"
        },
        "Jupiter-8 50mm f/2": {
            "description": "shot with Jupiter-8 50mm f/2 lens",
            "characteristics": "vintage Zeiss rendering, warm character, classic bokeh, Soviet optics aesthetic"
        },
        "Industar 61 L/Z 50mm f/2.8": {
            "description": "shot with Industar 61 50mm f/2.8 lens",
            "characteristics": "vintage pancake lens, compact rendering, retro aesthetic, budget classic character"
        },
        
        # Medium Format Lenses
        "Hasselblad Planar 80mm f/2.8": {
            "description": "shot with Hasselblad Planar 80mm f/2.8 lens",
            "characteristics": "medium format rendering, exceptional detail, smooth tonality, professional studio quality, Zeiss optics"
        },
        "Hasselblad Distagon 50mm f/4": {
            "description": "shot with Hasselblad Distagon 50mm f/4 lens",
            "characteristics": "medium format wide angle, controlled distortion, architectural precision, professional quality"
        },
        "Mamiya Sekor 80mm f/2.8": {
            "description": "shot with Mamiya Sekor 80mm f/2.8 lens",
            "characteristics": "medium format sharpness, professional portrait rendering, beautiful bokeh, studio standard"
        },
        "Pentax 67 105mm f/2.4": {
            "description": "shot with Pentax 67 105mm f/2.4 lens",
            "characteristics": "legendary bokeh, medium format compression, portrait perfection, dream lens aesthetic"
        },
        
        # Large Aperture Specialty
        "Voigtlander Nokton 50mm f/1.5": {
            "description": "shot with Voigtlander Nokton 50mm f/1.5 lens",
            "characteristics": "classic rendering, vintage bokeh, affordable quality, character-rich optics"
        },
        "Voigtlander Nokton 35mm f/1.4": {
            "description": "shot with Voigtlander Nokton 35mm f/1.4 lens",
            "characteristics": "wide aperture, classic rendering, vintage character, street photography lens"
        },
        "Meyer Optik Trioplan 100mm f/2.8": {
            "description": "shot with Meyer Optik Trioplan 100mm f/2.8 lens",
            "characteristics": "soap bubble bokeh, unique rendering, vintage character, artistic background blur"
        },
        
        # Modern Specialty
        "Sigma Art 35mm f/1.4": {
            "description": "shot with Sigma Art 35mm f/1.4 lens",
            "characteristics": "ultra sharp, modern rendering, wide aperture, professional quality, high resolution"
        },
        "Sigma Art 50mm f/1.4": {
            "description": "shot with Sigma Art 50mm f/1.4 lens",
            "characteristics": "extremely sharp, modern optics, creamy bokeh, professional standard"
        },
        "Sigma Art 85mm f/1.4": {
            "description": "shot with Sigma Art 85mm f/1.4 lens",
            "characteristics": "razor sharp, beautiful bokeh, modern portrait lens, professional quality"
        },
    }
    
    # Print Styles and Darkroom Processes
    CAMERA_FORMATS = {
        "None (Auto)": {
            "description": "",
            "characteristics": ""
        },
        
        # 35mm Film Formats
        "35mm Full Frame": {
            "description": "35mm full frame format",
            "characteristics": "24x36mm frame, standard 35mm photography, versatile format, popular aspect ratio"
        },
        "35mm Half Frame": {
            "description": "35mm half frame format",
            "characteristics": "18x24mm frame, vertical orientation, compact camera aesthetic, double exposures per frame"
        },
        
        # Medium Format
        "6x4.5 (645)": {
            "description": "6x4.5cm medium format",
            "characteristics": "645 aspect ratio, medium format quality, portable large format, professional wedding standard"
        },
        "6x6 Square Format": {
            "description": "6x6cm square format",
            "characteristics": "square composition, Hasselblad aesthetic, medium format quality, iconic 1:1 ratio, fashion photography standard"
        },
        "6x7 Format": {
            "description": "6x7cm medium format",
            "characteristics": "ideal format, near 4x5 ratio, Pentax 67 look, portrait photography standard, large negative quality"
        },
        "6x8 Format": {
            "description": "6x8cm medium format",
            "characteristics": "wide medium format, landscape orientation, Fuji rangefinder aesthetic"
        },
        "6x9 Format": {
            "description": "6x9cm medium format",
            "characteristics": "wide medium format frame, excellent detail, landscape photography, folder camera classic"
        },
        "6x12 Panoramic": {
            "description": "6x12cm panoramic format",
            "characteristics": "ultra-wide panoramic, sweeping vistas, landscape specialty, dramatic aspect ratio"
        },
        "6x17 Panoramic": {
            "description": "6x17cm panoramic format",
            "characteristics": "extreme panoramic format, ultra-wide landscapes, specialized photography, cinematic aspect"
        },
        
        # Large Format
        "4x5 Large Format": {
            "description": "4x5 inch large format",
            "characteristics": "sheet film quality, view camera aesthetic, architectural photography standard, exceptional detail, movements and tilts"
        },
        "5x7 Large Format": {
            "description": "5x7 inch large format",
            "characteristics": "large sheet film, portrait photography classic, contact print quality, vintage prestige"
        },
        "8x10 Large Format": {
            "description": "8x10 inch large format",
            "characteristics": "ultimate image quality, contact print standard, Ansel Adams format, landscape photography prestige, museum quality"
        },
        "11x14 Large Format": {
            "description": "11x14 inch ultra large format",
            "characteristics": "rare oversized format, exceptional contact prints, portrait studio prestige, turn of century aesthetic"
        },
        
        # Specialty Cameras
        "Polaroid SX-70 Format": {
            "description": "Polaroid SX-70 instant format",
            "characteristics": "square instant film, folding SLR aesthetic, 1970s design classic, white border frame"
        },
        "Polaroid Type 55 4x5": {
            "description": "Polaroid Type 55 4x5 instant",
            "characteristics": "instant positive and negative, professional testing film, fine grain quality, 1960s-2000s professional standard"
        },
        "Holga 120 Format": {
            "description": "Holga 120 toy camera format",
            "characteristics": "plastic lens vignetting, light leaks, lo-fi aesthetic, dreamy soft focus, cult classic imperfection"
        },
        "Diana Camera Format": {
            "description": "Diana toy camera format",
            "characteristics": "vintage toy camera, square or rectangular, unpredictable results, lo-fi charm, 1960s nostalgia"
        },
        "Lomography LC-A": {
            "description": "Lomo LC-A format",
            "characteristics": "35mm compact, high contrast, heavy vignetting, saturated colors, cult camera aesthetic"
        },
        
        # Historical Formats
        "Wet Plate 8x10": {
            "description": "8x10 wet plate collodion",
            "characteristics": "Civil War era process, glass plate negative, ethereal glow, hand-poured emulsion, 1850s-1880s technique"
        },
        "Dry Plate Photography": {
            "description": "gelatin dry plate photography",
            "characteristics": "1870s-1920s technique, glass negative, transitional process, Victorian era photography"
        },
        "Mammoth Plate": {
            "description": "mammoth plate photography",
            "characteristics": "oversized glass plates, 18x22 inches or larger, 19th century landscape photography, exceptional detail"
        },
        
        # Stereo and Panoramic
        "Stereo Pairs": {
            "description": "stereoscopic photography",
            "characteristics": "dual lens capture, 3D viewing cards, Victorian entertainment, side-by-side images"
        },
        "Panoramic Banquet Camera": {
            "description": "rotating panoramic camera",
            "characteristics": "curved group portraits, sweeping rotation, early 1900s group photography, distortion at edges"
        },
    }
    
    # Photography Eras and Movements
    PHOTOGRAPHY_ERAS = {
        "None (Contemporary)": {
            "description": "",
            "characteristics": ""
        },
        
        # 19th Century
        "1840s Daguerreian Era": {
            "description": "1840s daguerreotype era aesthetic",
            "characteristics": "earliest photography, posed portraits, long exposures, mirror-like plates, Victorian formality"
        },
        "1850s-1860s Wet Plate Era": {
            "description": "1850s-1860s wet plate collodion era",
            "characteristics": "Civil War photography, glass negatives, portable darkroom, Mathew Brady aesthetic"
        },
        "1860s-1880s Cartes de Visite": {
            "description": "cartes de visite portrait cards",
            "characteristics": "small portrait cards, Victorian social currency, album photographs, formal studio poses"
        },
        "1880s-1900s Pictorialism": {
            "description": "pictorialist photography movement",
            "characteristics": "soft focus, artistic manipulation, painterly quality, photography as fine art, salon prints"
        },
        
        # Early 20th Century
        "1900s-1920s Photo-Secession": {
            "description": "Photo-Secession movement aesthetic",
            "characteristics": "Alfred Stieglitz style, platinum prints, artistic photography, Camera Work quality"
        },
        "1920s-1930s Modernism": {
            "description": "modernist photography aesthetic",
            "characteristics": "sharp focus, geometric composition, industrial subjects, Man Ray style, avant-garde"
        },
        "1930s-1940s FSA Documentary": {
            "description": "FSA documentary photography style",
            "characteristics": "Great Depression era, social documentary, Dorothea Lange aesthetic, historical documentation, American life"
        },
        "1930s f/64 Group": {
            "description": "Group f/64 aesthetic",
            "characteristics": "maximum sharpness, straight photography, Ansel Adams style, Edward Weston precision, large format detail"
        },
        
        # Mid-20th Century
        "1940s-1950s Film Noir": {
            "description": "film noir photography aesthetic",
            "characteristics": "dramatic shadows, high contrast, urban night scenes, crime photography, moody atmosphere"
        },
        "1950s-1960s Street Photography": {
            "description": "classic street photography era",
            "characteristics": "Henri Cartier-Bresson decisive moment, Leica aesthetic, candid urban life, photojournalism"
        },
        "1960s-1970s New Color": {
            "description": "New Color photography movement",
            "characteristics": "William Eggleston aesthetic, Stephen Shore style, everyday America, color as subject, banal beauty"
        },
        "1970s Snapshot Aesthetic": {
            "description": "1970s snapshot photography",
            "characteristics": "vernacular photography, amateur aesthetic, family snapshots, Instamatic look, found photography"
        },
        
        # Late 20th Century  
        "1980s Fashion Photography": {
            "description": "1980s fashion photography aesthetic",
            "characteristics": "high gloss, studio lighting, Richard Avedon style, Helmut Newton drama, commercial perfection"
        },
        "1980s-1990s Grunge Photography": {
            "description": "grunge era photography",
            "characteristics": "raw aesthetic, DIY quality, zine culture, youth culture documentation, anti-polish"
        },
        "1990s Heroin Chic": {
            "description": "1990s fashion photography style",
            "characteristics": "desaturated, raw flash, anti-glamour, Corinne Day aesthetic, controversial fashion"
        },
        
        # Contemporary Movements
        "Contemporary Fine Art": {
            "description": "contemporary fine art photography",
            "characteristics": "conceptual approach, large format prints, gallery quality, artistic intention, museum standard"
        },
        "Documentary Realism": {
            "description": "documentary realism style",
            "characteristics": "objective observation, social issues, photojournalism ethics, truth-telling aesthetic"
        },
    }
    
    # Lighting Techniques and Styles
    LIGHTING_STYLES = {
        "None (Natural)": {
            "description": "",
            "characteristics": ""
        },
        
        # Historical Lighting
        "Magnesium Flash (1880s-1920s)": {
            "description": "magnesium flash powder lighting",
            "characteristics": "harsh frontal light, deep shadows, vintage studio aesthetic, early flash photography, explosive illumination"
        },
        "Hot Lights Studio (1920s-1950s)": {
            "description": "hot tungsten studio lighting",
            "characteristics": "warm color temperature, continuous lighting, Hollywood golden age, soft shadows, classic studio portrait lighting"
        },
        "Flashbulb Era (1930s-1970s)": {
            "description": "single-use flashbulb lighting",
            "characteristics": "bright frontal flash, press photography aesthetic, mid-century photojournalism, one-shot lighting"
        },
        
        # Studio Lighting Setups
        "Rembrandt Lighting": {
            "description": "Rembrandt lighting setup",
            "characteristics": "triangular highlight on cheek, dramatic shadows, 45-degree key light, classic portrait lighting, chiaroscuro effect"
        },
        "Butterfly Lighting": {
            "description": "butterfly lighting setup",
            "characteristics": "butterfly shadow under nose, beauty lighting, glamour photography, high frontal key light, symmetrical shadows"
        },
        "Split Lighting": {
            "description": "split lighting setup",
            "characteristics": "half face lit half in shadow, dramatic portrait, 90-degree side light, masculine aesthetic, high contrast"
        },
        "Loop Lighting": {
            "description": "loop lighting setup",
            "characteristics": "small nose shadow, natural portrait look, slight shadow loop, professional headshot lighting"
        },
        "Broad Lighting": {
            "description": "broad lighting setup",
            "characteristics": "lit side of face toward camera, wider face appearance, commercial portrait style"
        },
        "Short Lighting": {
            "description": "short lighting setup",
            "characteristics": "shadow side of face toward camera, slimming effect, dramatic portrait, sculptural shadows"
        },
        
        # Fashion & Commercial Lighting
        "Clamshell Lighting": {
            "description": "clamshell beauty lighting",
            "characteristics": "top and bottom fill, glamour photography, beauty dish aesthetic, even facial illumination, catchlights in eyes"
        },
        "High Key Lighting": {
            "description": "high key lighting setup",
            "characteristics": "bright even illumination, minimal shadows, white background aesthetic, commercial photography, optimistic mood"
        },
        "Low Key Lighting": {
            "description": "low key lighting setup",
            "characteristics": "predominantly dark tones, dramatic shadows, film noir aesthetic, moody atmosphere, selective illumination"
        },
        "Ring Light": {
            "description": "ring light illumination",
            "characteristics": "circular catchlight, fashion photography, even frontal light, signature eye reflection, modern portrait style"
        },
        
        # Natural Light Styles
        "Window Light Portrait": {
            "description": "natural window light",
            "characteristics": "soft directional light, Vermeer quality, fine art portrait, gentle shadows, available light aesthetic"
        },
        "Golden Hour": {
            "description": "golden hour natural light",
            "characteristics": "warm amber tones, soft shadows, magic hour glow, horizontal sunlight, romantic atmosphere"
        },
        "Blue Hour": {
            "description": "blue hour twilight",
            "characteristics": "cool blue tones, even ambient light, dusk atmosphere, minimal shadows, ethereal quality"
        },
        "Overcast Diffused": {
            "description": "overcast natural diffusion",
            "characteristics": "soft shadowless light, even illumination, cloudy day aesthetic, gentle tones, portrait friendly"
        },
        "Direct Sunlight": {
            "description": "direct harsh sunlight",
            "characteristics": "hard shadows, high contrast, midday sun, dramatic lighting, strong directional light"
        },
        
        # Cinematic Lighting
        "Film Noir Lighting": {
            "description": "film noir dramatic lighting",
            "characteristics": "venetian blind shadows, hard side light, crime scene aesthetic, 1940s mystery, stark contrast"
        },
        "Practical Lighting": {
            "description": "practical light sources",
            "characteristics": "visible light sources in frame, lamp-lit scenes, ambient environmental light, natural motivation, cinematic realism"
        },
        "Bounce Light": {
            "description": "bounced reflected lighting",
            "characteristics": "soft indirect illumination, natural fall-off, reflected light quality, subtle shadows, documentary style"
        },
        
        # Flash Techniques
        "Direct On-Camera Flash": {
            "description": "direct on-camera flash",
            "characteristics": "flat frontal lighting, snapshot aesthetic, harsh shadows, paparazzi style, amateur flash photography"
        },
        "Bounce Flash": {
            "description": "bounced ceiling flash",
            "characteristics": "soft indirect flash, wedding photography, natural-looking flash, even illumination"
        },
        "Off-Camera Flash": {
            "description": "off-camera flash lighting",
            "characteristics": "directional flash, professional event photography, balanced exposure, sculpted light"
        },
        "Strobist Lighting": {
            "description": "multiple off-camera strobes",
            "characteristics": "complex flash setup, dramatic effect, location lighting, modern editorial style"
        },
    }
    
    # Photography Genres and Styles
    PHOTOGRAPHY_GENRES = {
        "None (General)": {
            "description": "",
            "characteristics": ""
        },
        
        # Documentary & Journalism
        "Photojournalism": {
            "description": "photojournalism style",
            "characteristics": "decisive moment, candid captures, editorial integrity, news documentation, unposed authenticity, storytelling priority"
        },
        "War Photography": {
            "description": "war photography documentation",
            "characteristics": "conflict documentation, harsh reality, historical record, combat zone aesthetic, gritty realism, emotional impact"
        },
        "Social Documentary": {
            "description": "social documentary photography",
            "characteristics": "human condition focus, empathetic observation, cultural documentation, FSA tradition, social issues, long-term projects"
        },
        "Street Photography": {
            "description": "street photography style",
            "characteristics": "urban candid moments, decisive moment, found compositions, everyday life, unposed subjects, public space documentation"
        },
        
        # Portrait Styles
        "Studio Portrait": {
            "description": "formal studio portrait",
            "characteristics": "controlled lighting, solid background, posed composition, professional quality, headshot aesthetic"
        },
        "Environmental Portrait": {
            "description": "environmental portrait",
            "characteristics": "subject in context, location revealing character, natural setting, storytelling background, narrative composition"
        },
        "Fashion Photography": {
            "description": "fashion photography editorial",
            "characteristics": "haute couture aesthetic, model poses, clothing showcase, high production value, stylized composition, runway influence"
        },
        "Beauty Photography": {
            "description": "beauty photography closeup",
            "characteristics": "makeup emphasis, skin detail, cosmetic advertising, tight framing, perfect retouching, commercial glamour"
        },
        "Glamour Photography": {
            "description": "glamour photography style",
            "characteristics": "idealized beauty, soft focus options, flattering lighting, elegant poses, aspirational aesthetic"
        },
        
        # Landscape & Nature
        "Landscape Photography": {
            "description": "landscape photography",
            "characteristics": "grand vistas, natural world, wide compositions, environmental scale, light and atmosphere, patient timing"
        },
        "Seascape": {
            "description": "seascape photography",
            "characteristics": "ocean and coast, long exposures, water movement, maritime atmosphere, horizon emphasis"
        },
        "Aerial Photography": {
            "description": "aerial photography",
            "characteristics": "bird's eye view, abstract patterns, landscape from above, unique perspective, geometric compositions"
        },
        "Wildlife Photography": {
            "description": "wildlife photography",
            "characteristics": "animal behavior, natural habitat, telephoto compression, National Geographic style, patience and timing"
        },
        "Macro Photography": {
            "description": "macro photography closeup",
            "characteristics": "extreme detail, shallow depth of field, small subject large, abstract texture, scientific observation"
        },
        
        # Architectural & Interior
        "Architectural Photography": {
            "description": "architectural photography",
            "characteristics": "building documentation, perspective control, geometric precision, structural emphasis, tilt-shift aesthetic, clean lines"
        },
        "Interior Photography": {
            "description": "interior photography",
            "characteristics": "space documentation, ambient light balance, room atmosphere, real estate aesthetic, wide angle coverage"
        },
        "Urban Exploration": {
            "description": "urban exploration photography",
            "characteristics": "abandoned places, decay documentation, architectural ruins, atmospheric deterioration, forgotten spaces"
        },
        
        # Still Life & Product
        "Still Life": {
            "description": "still life photography",
            "characteristics": "arranged objects, controlled composition, studio craftsmanship, classic painting influence, careful arrangement"
        },
        "Product Photography": {
            "description": "commercial product photography",
            "characteristics": "clean backgrounds, detail emphasis, commercial clarity, catalog aesthetic, perfect presentation"
        },
        "Food Photography": {
            "description": "food photography",
            "characteristics": "culinary presentation, appetite appeal, shallow depth of field, natural light preference, editorial styling"
        },
        "Tabletop Photography": {
            "description": "tabletop studio photography",
            "characteristics": "small scale setup, controlled environment, advertising quality, precise lighting, miniature world"
        },
        
        # Scientific & Technical
        "Scientific Photography": {
            "description": "scientific documentation photography",
            "characteristics": "objective documentation, clinical lighting, specimen photography, educational purpose, technical accuracy"
        },
        "Medical Photography": {
            "description": "medical documentation photography",
            "characteristics": "clinical documentation, diagnostic purpose, neutral lighting, technical precision, educational record"
        },
        "Forensic Photography": {
            "description": "forensic documentation",
            "characteristics": "crime scene documentation, evidence photography, objective record, scale reference, systematic coverage"
        },
        
        # Conceptual & Fine Art
        "Fine Art Photography": {
            "description": "fine art photography",
            "characteristics": "artistic vision, personal expression, gallery presentation, limited editions, conceptual depth, museum quality"
        },
        "Conceptual Photography": {
            "description": "conceptual art photography",
            "characteristics": "idea-driven imagery, symbolic content, artistic statement, narrative construction, intellectual engagement"
        },
        "Surreal Photography": {
            "description": "surrealist photography",
            "characteristics": "dreamlike imagery, impossible scenes, reality manipulation, subconscious exploration, fantasy aesthetic"
        },
        "Minimalist Photography": {
            "description": "minimalist photography",
            "characteristics": "simplified composition, negative space, essential elements only, zen aesthetic, clean lines, subtle tones"
        },
        
        # Event & Lifestyle
        "Wedding Photography": {
            "description": "wedding photography",
            "characteristics": "romantic moments, emotional documentation, posed and candid mix, soft flattering light, celebration atmosphere"
        },
        "Event Photography": {
            "description": "event documentation photography",
            "characteristics": "moment capture, crowd documentation, ambient light work, coverage shooting, storytelling sequence"
        },
        "Lifestyle Photography": {
            "description": "lifestyle photography",
            "characteristics": "authentic moments, natural interactions, commercial but candid, aspirational everyday life, brand storytelling"
        },
    }
    
    # Technical Processes and Darkroom Techniques
    TECHNICAL_PROCESSES = {
        "None (Standard Processing)": {
            "description": "",
            "characteristics": ""
        },
        
        # Push/Pull Processing
        "Push +1 Stop": {
            "description": "push processed +1 stop",
            "characteristics": "increased grain, higher contrast, extended shadow detail, underexposure compensation, gritty aesthetic"
        },
        "Push +2 Stops": {
            "description": "push processed +2 stops",
            "characteristics": "heavy grain, extreme contrast, blown highlights, dramatic blacks, experimental aesthetic, low light solution"
        },
        "Push +3 Stops": {
            "description": "push processed +3 stops",
            "characteristics": "extreme grain, harsh contrast, degraded highlights, intense blacks, punk rock aesthetic, desperate exposure"
        },
        "Pull -1 Stop": {
            "description": "pull processed -1 stop",
            "characteristics": "fine grain, reduced contrast, overexposure correction, pastel tones, delicate shadows"
        },
        
        # Cross Processing
        "Cross Process (E-6 in C-41)": {
            "description": "cross processed slide film in C-41",
            "characteristics": "saturated colors, color shifts, high contrast, cyan shadows yellow highlights, fashion editorial look, 1990s aesthetic"
        },
        "Cross Process (C-41 in E-6)": {
            "description": "cross processed negative film in E-6",
            "characteristics": "desaturated colors, unusual color casts, flat contrast, experimental tones, alternative process look"
        },
        
        # Special Processing
        "Bleach Bypass (ENR/CCE)": {
            "description": "bleach bypass processing",
            "characteristics": "high contrast, desaturated color, retained silver, gritty cinematic look, crushed blacks, thriller aesthetic"
        },
        "Redscale": {
            "description": "redscale film technique",
            "characteristics": "red-orange-yellow color shift, reversed emulsion, warm cast, experimental color, lomography aesthetic"
        },
        "Expired Film": {
            "description": "expired film stock",
            "characteristics": "color shifts, reduced contrast, unpredictable results, faded colors, nostalgic degradation, vintage accidents"
        },
        "Cold Storage Film": {
            "description": "refrigerated film stock",
            "characteristics": "preserved color accuracy, fine grain retention, professional archival, optimal characteristics"
        },
        
        # Multiple Exposure
        "Double Exposure": {
            "description": "double exposure technique",
            "characteristics": "layered images, ghostly overlay, experimental composition, surreal combination, film rewind technique"
        },
        "Multiple Exposure": {
            "description": "multiple exposure layering",
            "characteristics": "complex image overlay, experimental narrative, motion study, time compression, abstract patterns"
        },
        
        # Darkroom Manipulation
        "Dodging and Burning": {
            "description": "selective dodging and burning",
            "characteristics": "localized exposure control, enhanced drama, Ansel Adams technique, sculptural lighting, fine art printing"
        },
        "Solarization (Sabattier Effect)": {
            "description": "solarization darkroom technique",
            "characteristics": "tone reversal, edge lines, surreal effect, Man Ray technique, experimental aesthetic, partial reversal"
        },
        "Hand Coloring": {
            "description": "hand colored photograph",
            "characteristics": "painted color on B&W, selective colorization, folk art aesthetic, Victorian tradition, artisan craft"
        },
        "Toning Variations": {
            "description": "chemical toning process",
            "characteristics": "color cast from toning salts, archival treatment, artistic coloration, varied metal tones"
        },
        
        # Experimental Techniques
        "Photogram": {
            "description": "camera-less photogram",
            "characteristics": "direct object on paper, Man Ray rayographs, silhouette imagery, experimental process, shadow play"
        },
        "Chemigram": {
            "description": "chemigram technique",
            "characteristics": "chemical resist patterns, abstract imagery, experimental process, unpredictable results, painterly chemistry"
        },
        "Lumen Print": {
            "description": "lumen print process",
            "characteristics": "sun printing, no developer, organic decay imagery, botanical prints, unstable colors, ephemeral quality"
        },
        
        # Film Scanning/Transfer
        "Frontier Scan Aesthetic": {
            "description": "Frontier film scanner look",
            "characteristics": "clean scan, neutral color, professional lab standard, accurate rendition, modern film digitization"
        },
        "Noritsu Scan Aesthetic": {
            "description": "Noritsu film scanner look",
            "characteristics": "warm scan tendency, consumer lab aesthetic, slightly soft, nostalgic digitization"
        },
        "Flatbed Scan": {
            "description": "flatbed scanner film capture",
            "characteristics": "soft detail, muted colors, home scanning aesthetic, accessible digitization, DIY quality"
        },
        "Drum Scan": {
            "description": "drum scanner capture",
            "characteristics": "maximum resolution, perfect color, museum quality digitization, professional archival, finest detail"
        },
    }
    
    # Damage and Aging Effects
    DAMAGE_EFFECTS = {
        "None (Pristine)": {
            "description": "",
            "characteristics": ""
        },
        
        # Physical Damage
        "Light Leaks": {
            "description": "film light leak damage",
            "characteristics": "orange-red light streaks, accidental exposure, vintage camera flaws, lomography aesthetic, serendipitous artifacts"
        },
        "Scratches and Dust": {
            "description": "film scratches and dust artifacts",
            "characteristics": "vertical scratches, dust spots, handling wear, archival degradation, authentic film texture"
        },
        "Sprocket Holes Visible": {
            "description": "sprocket hole cinema aesthetic",
            "characteristics": "film perforations in frame, full frame exposure, cinema film look, wide panoramic, experimental framing"
        },
        "Edge Markings": {
            "description": "film edge code visible",
            "characteristics": "manufacturer markings, frame numbers, technical inscriptions, film stock identification, professional workflow"
        },
        "Film Gate Vignetting": {
            "description": "camera gate vignetting",
            "characteristics": "rounded corner darkening, lens falloff, vintage camera characteristic, organic frame edge, optical limitation"
        },
        
        # Chemical Deterioration
        "Faded Color Shift": {
            "description": "aged color photograph fading",
            "characteristics": "magenta color cast, cyan loss, yellow shift, decades of aging, deteriorated dyes, nostalgic decay"
        },
        "Yellowed Paper": {
            "description": "aged yellowed photographic paper",
            "characteristics": "warm yellow cast, vintage patina, oxidation, archival aging, antique photograph feel"
        },
        "Vinegar Syndrome": {
            "description": "acetate film decay",
            "characteristics": "color shifts, base deterioration, archival emergency, acidic degradation, historical film damage"
        },
        "Fungus on Lens": {
            "description": "lens fungus optical damage",
            "characteristics": "soft focus areas, contrast loss, hazy bloom, tropical climate damage, organic growth patterns"
        },
        "Silver Mirroring": {
            "description": "silver gelatin mirroring",
            "characteristics": "metallic sheen in shadows, reflective deterioration, archival degradation, mirror-like patches"
        },
        
        # Environmental Damage
        "Water Damage": {
            "description": "water damaged photograph",
            "characteristics": "staining patterns, emulsion lifting, tide marks, flood damage, irregular deterioration, disaster recovery"
        },
        "Fire/Heat Damage": {
            "description": "heat damaged photograph",
            "characteristics": "warped emulsion, color shifts, bubbling, heat exposure, disaster salvage, melted areas"
        },
        "Mold Damage": {
            "description": "mold damaged photograph",
            "characteristics": "irregular staining, organic patterns, humidity damage, biological growth, archival neglect"
        },
        
        # Mechanical Wear
        "Creases and Folds": {
            "description": "creased folded photograph",
            "characteristics": "white fold lines, handling damage, wallet wear, bent corners, lived-in quality, personal history"
        },
        "Edge Wear": {
            "description": "worn photograph edges",
            "characteristics": "tattered borders, handling damage, album removed, vintage condition, time-worn appearance"
        },
        "Tape and Adhesive Marks": {
            "description": "adhesive damage",
            "characteristics": "tape residue, mounting evidence, yellowed tape, scrapbook remnants, archival violation"
        },
        
        # Analog Artifacts
        "Film Grain Emphasis": {
            "description": "emphasized film grain",
            "characteristics": "visible grain structure, textured surface, high ISO push, enlarged detail, analog texture"
        },
        "Motion Blur": {
            "description": "motion blur",
            "characteristics": "subject movement, slow shutter, dynamic energy, action blur, intentional motion, time passage"
        },
        "Out of Focus": {
            "description": "focus error",
            "characteristics": "missed focus, soft detail, focusing mistake, dreamy unsharpness, snapshot accident"
        },
        "Overexposure Blow-out": {
            "description": "overexposed highlights",
            "characteristics": "blown highlights, detail loss, exposure mistake, harsh lighting, clipped whites"
        },
        "Underexposure Murk": {
            "description": "underexposed shadows",
            "characteristics": "blocked shadows, dark murkiness, exposure error, low light failure, crushed blacks"
        },
        
        # Nostalgic Patina
        "Vintage Patina Overall": {
            "description": "overall vintage patina",
            "characteristics": "subtle aging, gentle fading, nostalgic warmth, time-softened, heirloom quality, gentle deterioration"
        },
        "Archival Foxing": {
            "description": "foxing spots on paper",
            "characteristics": "brown age spots, paper deterioration, antique condition, organic staining, historical document feel"
        },
    }
    
    # Famous Photographer Signature Styles
    PHOTOGRAPHER_STYLES = {
        "None (Original Style)": {
            "description": "",
            "characteristics": ""
        },
        
        # Masters of Black & White
        "Ansel Adams Style": {
            "description": "Ansel Adams aesthetic",
            "characteristics": "zone system precision, f/64 sharpness, dramatic landscapes, perfect tonal range, large format quality, American West, patient composition. Equipment: 8x10 view camera, B&W film developed with zone system, small aperture f/64"
        },
        "Henri Cartier-Bresson Style": {
            "description": "Henri Cartier-Bresson decisive moment",
            "characteristics": "35mm Leica aesthetic, geometric composition, perfect timing, street photography, candid humanist, unposed life, European streets. Equipment: Leica rangefinder 35mm or 50mm lens, B&W film (HP5/Tri-X), natural light only"
        },
        "Diane Arbus Style": {
            "description": "Diane Arbus aesthetic",
            "characteristics": "square format, direct gaze, outsider subjects, unflinching honesty, flash-lit portraits, psychological intensity, American subcultures. Equipment: Rolleiflex twin-lens reflex 6x6, Tri-X 400, on-camera flash"
        },
        "Irving Penn Style": {
            "description": "Irving Penn aesthetic",
            "characteristics": "white seamless background, corner portraits, still life mastery, studio perfection, commercial elegance, Vogue quality, sculptural lighting. Equipment: 8x10 view camera, controlled studio lighting, platinum prints"
        },
        "Richard Avedon Style": {
            "description": "Richard Avedon aesthetic",
            "characteristics": "white background portraits, 8x10 large format, unflinching detail, fashion and portraiture, psychological depth, In the American West. Equipment: Deardorff 8x10 view camera, strobe lighting, stark white seamless"
        },
        "Annie Leibovitz Style": {
            "description": "Annie Leibovitz aesthetic",
            "characteristics": "environmental portraits, celebrity photography, narrative staging, dramatic lighting, Vanity Fair aesthetic, storytelling composition, elaborate productions. Equipment: Medium format (Mamiya RZ67), natural and studio lighting mixed, color and B&W"
        },
        "Robert Mapplethorpe Style": {
            "description": "Robert Mapplethorpe aesthetic",
            "characteristics": "formal composition, classical sculpture influence, perfect printing, controversial subjects, studio precision, Hasselblad medium format. Equipment: Hasselblad 500C/M medium format, studio lighting, platinum and silver gelatin prints"
        },
        "Sebastião Salgado Style": {
            "description": "Sebastião Salgado aesthetic",
            "characteristics": "epic social documentary, dramatic contrast, humanitarian focus, worker portraits, large format black and white, global perspective. Equipment: 35mm and medium format, B&W film, natural light, long-term projects"
        },
        "Nan Goldin Style": {
            "description": "Nan Goldin aesthetic",
            "characteristics": "intimate diary photography, raw emotional honesty, snapshot aesthetic, natural light, LGBTQ+ life documentation, The Ballad of Sexual Dependency, unposed authenticity. Equipment: 35mm point-and-shoot or SLR, Kodachrome slides (early), Cibachrome prints, on-camera flash, available light"
        },
        "Josef Koudelka Style": {
            "description": "Josef Koudelka aesthetic",
            "characteristics": "panoramic black and white, Roma and Czech documentation, Exiles series, dramatic sky and landscape, wide format compositions, nomadic perspective, poetic witnessing. Equipment: Leica 35mm with 25mm lens (early), later panoramic cameras, B&W film (Tri-X), natural light"
        },
        "Mary Ellen Mark Style": {
            "description": "Mary Ellen Mark aesthetic",
            "characteristics": "humanist documentary, social margins, empathetic portraits, black and white, circus and street life, compassionate observation, American subcultures, intimate access. Equipment: 35mm (Leica), later medium format, Tri-X 400, available light and minimal flash"
        },
        
        # Color Photography Masters
        "William Eggleston Style": {
            "description": "William Eggleston aesthetic",
            "characteristics": "dye transfer prints, mundane subjects elevated, democratic photography, Memphis Tennessee, everyday America, color as subject, deadpan composition. Equipment: 35mm (Leica), later medium format, Kodachrome slides, dye-transfer printing process"
        },
        "Stephen Shore Style": {
            "description": "Stephen Shore aesthetic",
            "characteristics": "large format color, banal beauty, American vernacular, roadside America, deadpan aesthetic, meticulous composition, 1970s New Color. Equipment: 4x5 and 8x10 view cameras, color negative film, C-prints, tripod-based precision"
        },
        "Saul Leiter Style": {
            "description": "Saul Leiter aesthetic",
            "characteristics": "abstract color compositions, reflections and layers, painterly quality, New York street, windows and rain, pioneering color work, intimate observations. Equipment: 35mm Leica, Kodachrome slides, natural light, shot through windows and rain"
        },
        "Steve McCurry Style": {
            "description": "Steve McCurry aesthetic",
            "characteristics": "saturated Kodachrome, National Geographic quality, cultural portraiture, Afghan Girl iconic, travel photography, vivid storytelling, global humanity. Equipment: 35mm Nikon, Kodachrome 64, natural light, extensive travel"
        },
        "Alex Webb Style": {
            "description": "Alex Webb aesthetic",
            "characteristics": "layered color complexity, tropical light, multiple planes of focus, street photography, Magnum aesthetic, saturated color, Caribbean and Latin America, complex compositions. Equipment: 35mm rangefinder (Leica), wide angle lenses (28mm), Kodachrome, harsh sunlight"
        },
        
        # Fashion Photography
        "Helmut Newton Style": {
            "description": "Helmut Newton aesthetic",
            "characteristics": "high contrast black and white, provocative fashion, powerful women, 1970s-80s edge, noir influence, controversial glamour, architectural settings. Equipment: Medium format (Hasselblad, Mamiya RZ67), studio strobes, stark lighting, large prints"
        },
        "Guy Bourdin Style": {
            "description": "Guy Bourdin aesthetic",
            "characteristics": "surreal fashion, narrative mystery, vivid color, French Vogue, provocative staging, cinematic influence, psychological tension. Equipment: Medium format, color negative, elaborate staging, Vogue fashion shoots"
        },
        "Peter Lindbergh Style": {
            "description": "Peter Lindbergh aesthetic",
            "characteristics": "black and white fashion, raw beauty, anti-retouching, supermodel era, emotional honesty, natural light preference, 1990s revolution. Equipment: Medium format (Pentax 67, Mamiya), B&W film, natural and available light, minimal retouching"
        },
        "Jo Ann Callis Style": {
            "description": "Jo Ann Callis aesthetic",
            "characteristics": "staged domestic scenes, saturated color, surreal narrative, feminist perspective, 1970s-80s Los Angeles, mysterious interiors, theatrical lighting. Equipment: 4x5 view camera, color negative (Ektacolor), controlled studio lighting, constructed sets"
        },
        "Rineke Dijkstra Style": {
            "description": "Rineke Dijkstra aesthetic",
            "characteristics": "large format color portraits, beach series, direct frontal pose, young people transitions, clinical precision, neutral backgrounds, psychological depth. Equipment: 4x5 view camera, color negative film, natural overcast light, tripod, beach portraits"
        },
        
        # Documentary & Photojournalism
        "Dorothea Lange Style": {
            "description": "Dorothea Lange aesthetic",
            "characteristics": "FSA documentary, Great Depression, Migrant Mother iconic, social conscience, empathetic observation, large format documentary, American hardship. Equipment: 4x5 Graflex, later Rolleiflex, B&W film, natural light, FSA government project"
        },
        "Walker Evans Style": {
            "description": "Walker Evans aesthetic",
            "characteristics": "American vernacular, FSA documentation, straight photography, architectural detail, Depression era, objective observation, large format precision. Equipment: 8x10 view camera, 4x5 Deardorff, B&W film, available light, tripod-based"
        },
        "W. Eugene Smith Style": {
            "description": "W. Eugene Smith aesthetic",
            "characteristics": "photo essay mastery, LIFE magazine, dramatic lighting, humanitarian focus, Minamata series, ethical journalism, passionate advocacy. Equipment: 35mm Leica and Nikon, available light and flash, B&W film, LIFE magazine essays"
        },
        "James Nachtwey Style": {
            "description": "James Nachtwey aesthetic",
            "characteristics": "war photography, ethical documentation, black and white preference, witness to conflict, humanitarian concern, TIME magazine, powerful testimony. Equipment: 35mm Canon and Nikon, B&W and color, available light, conflict zones"
        },
        "Robert Capa Style": {
            "description": "Robert Capa aesthetic",
            "characteristics": "war photography pioneer, D-Day Normandy, slightly out of focus, in the action, Magnum co-founder, Spanish Civil War, courage and proximity. Equipment: 35mm Contax and Leica, B&W film, in the thick of action, handheld combat photography"
        },
        
        # Street Photography
        "Garry Winogrand Style": {
            "description": "Garry Winogrand aesthetic",
            "characteristics": "wide angle street, tilted horizons, 1960s-70s America, social landscape, continuous shooting, snapshot aesthetic, American chaos. Equipment: 35mm Leica M4 with 28mm lens, Tri-X, rapid shooting, tilted framing"
        },
        "Joel Meyerowitz Style": {
            "description": "Joel Meyerowitz aesthetic",
            "characteristics": "color street photography, large format later work, Cape Light series, New York street life, pioneering color, lyrical observation. Equipment: 35mm Leica (early street), later 8x10 view camera, color film, natural light"
        },
        "Vivian Maier Style": {
            "description": "Vivian Maier aesthetic",
            "characteristics": "nanny photographer, Rolleiflex square format, Chicago street life, posthumous discovery, self-portraits in reflections, 1950s-70s America. Equipment: Rolleiflex TLR 6x6, B&W and color film, waist-level viewfinder, undiscovered archive"
        },
        "Anders Petersen Style": {
            "description": "Anders Petersen aesthetic",
            "characteristics": "raw intimacy, black and white grain, Café Lehmitz series, human vulnerability, close proximity, Swedish documentary, nightlife photography, emotional intensity. Equipment: 35mm Leica, Tri-X pushed, available light and flash, close intimate distance"
        },
        "Bruce Gilden Style": {
            "description": "Bruce Gilden aesthetic",
            "characteristics": "confrontational flash, extreme close-up, in-your-face street photography, New York grit, direct flash on camera, unflinching portraits, aggressive proximity. Equipment: 35mm SLR or rangefinder, wide angle (28mm), on-camera flash (direct), Tri-X pushed, close proximity"
        },
        "Martin Parr Style": {
            "description": "Martin Parr aesthetic",
            "characteristics": "saturated color, social documentary, British seaside, ring flash aesthetic, consumerism critique, ironic observation, mundane elevated, Magnum documentary. Equipment: Medium format (Mamiya 7), later Macro ring flash on 35mm, color negative, saturated processing"
        },
        
        # Contemporary & Conceptual
        "Cindy Sherman Style": {
            "description": "Cindy Sherman aesthetic",
            "characteristics": "conceptual self-portraits, costume and character, film stills series, identity exploration, theatrical staging, postmodern photography. Equipment: Medium format (Hasselblad, Mamiya), color film, self-timer, elaborate costumes and makeup"
        },
        "Andreas Gursky Style": {
            "description": "Andreas Gursky aesthetic",
            "characteristics": "large scale prints, elevated perspective, pattern and repetition, digital manipulation, economic systems, Düsseldorf School, contemporary monumentality. Equipment: Large format view camera, digital post-production, massive prints (up to 12 feet), elevated vantage points"
        },
        "Gregory Crewdson Style": {
            "description": "Gregory Crewdson aesthetic",
            "characteristics": "cinematic staging, suburban America, elaborate production, twilight atmosphere, Edward Hopper influence, narrative ambiguity, film crew scale. Equipment: 8x10 view camera, elaborate lighting rigs, film crew production, constructed narratives"
        },
        "Kat Toronto Style": {
            "description": "Kat Toronto aesthetic",
            "characteristics": "intimate portrait photography, natural light, emotional vulnerability, queer identity, documentary intimacy, contemporary snapshot aesthetic, authentic moments. Equipment: 35mm and medium format, color and B&W, natural light, intimate proximity"
        },
        "Todd Hido Style": {
            "description": "Todd Hido aesthetic",
            "characteristics": "nocturnal suburbia, glowing windows at night, melancholic atmosphere, fog and rain, lonely houses, American loneliness, cinematic color, mysterious narratives. Equipment: 4x5 view camera, color negative film, night photography, car-based shooting, long exposures"
        },
        "Alex Prager Style": {
            "description": "Alex Prager aesthetic",
            "characteristics": "cinematic color staging, 1950s-60s Hollywood influence, elaborate productions, vivid saturated color, crowd scenes, psychological tension, retro glamour. Equipment: Medium and large format, elaborate staging, vivid color film/digital, Hollywood-scale production"
        },
        "Jeff Wall Style": {
            "description": "Jeff Wall aesthetic",
            "characteristics": "staged tableaux photography, backlit transparency, cinematic composition, art history references, constructed reality, large scale lightboxes, Vancouver School. Equipment: 8x10 view camera, later digital, backlit Cibachrome transparencies, meticulous staging"
        },
        
        # Japanese Photography
        "Daido Moriyama Style": {
            "description": "Daido Moriyama aesthetic",
            "characteristics": "high contrast grain, blurred motion, Tokyo streets, Provoke era, raw energy, snapshot aesthetic, urban alienation, 1960s-70s Japan. Equipment: Ricoh GR compact 28mm (iconic), Tri-X pushed to 1600, harsh contrast printing, handheld motion blur"
        },
        "Nobuyoshi Araki Style": {
            "description": "Nobuyoshi Araki aesthetic",
            "characteristics": "intimate diary, Tokyo documentation, Sentimental Journey, prolific output, personal mythology, Japanese urban life. Equipment: Compact 35mm cameras, B&W and color, snapshot approach, daily documentation"
        },
        
        # Modernist & Experimental
        "Man Ray Style": {
            "description": "Man Ray aesthetic",
            "characteristics": "surrealist photography, rayographs, photograms, solarization, experimental techniques, Dada influence, avant-garde Paris, camera-less photography. Equipment: Camera-less photograms, solarization in darkroom, experimental techniques, 1920s Paris avant-garde"
        },
        
        # Landscape Specialists
        "Edward Weston Style": {
            "description": "Edward Weston aesthetic",
            "characteristics": "f/64 group, form and texture, peppers and shells, contact prints, 8x10 large format, pure photography, modernist seeing. Equipment: 8x10 view camera, contact prints (no enlargement), f/64 aperture, natural light, precise focus"
        },
        "Minor White Style": {
            "description": "Minor White aesthetic",
            "characteristics": "zone system, spiritual landscapes, equivalent concept, abstract natural forms, meditation on seeing, teaching legacy. Equipment: 4x5 and 8x10 view cameras, B&W film, zone system development, contemplative approach"
        },
    }
    
    # Film stock definitions with their characteristics
    FILM_STOCKS = {
        # Black & White Films
        "Kodak Tri-X 400": {
            "description": "shot on Kodak Tri-X 400 black and white film",
            "characteristics": "high contrast, pronounced grain structure, deep blacks, crisp whites, gritty texture, classic street photography aesthetic"
        },
        "Ilford HP5 Plus 400": {
            "description": "shot on Ilford HP5 Plus 400 black and white film",
            "characteristics": "medium contrast, fine grain, smooth tonal gradation, rich midtones, versatile exposure latitude"
        },
        "Ilford Delta 3200": {
            "description": "shot on Ilford Delta 3200 black and white film",
            "characteristics": "very high speed, heavy grain, dramatic contrast, intense shadows, atmospheric mood, low-light aesthetic"
        },
        "Kodak T-Max 100": {
            "description": "shot on Kodak T-Max 100 black and white film",
            "characteristics": "extremely fine grain, sharp detail, smooth tonality, excellent sharpness, studio quality"
        },
        "Ilford FP4 Plus 125": {
            "description": "shot on Ilford FP4 Plus 125 black and white film",
            "characteristics": "fine grain, excellent sharpness, balanced contrast, classic aesthetic, smooth gray scale"
        },
        "Fomapan 400": {
            "description": "shot on Fomapan 400 black and white film",
            "characteristics": "vintage character, visible grain, old-school look, moderate contrast, nostalgic feel"
        },
        
        # Color Negative Films
        "Kodak Portra 400": {
            "description": "shot on Kodak Portra 400 color negative film",
            "characteristics": "natural skin tones, fine grain, pastel colors, soft contrast, subtle color palette, professional portrait quality"
        },
        "Kodak Portra 160": {
            "description": "shot on Kodak Portra 160 color negative film",
            "characteristics": "ultra fine grain, vibrant yet natural colors, excellent skin tones, smooth gradation, warm undertones"
        },
        "Kodak Portra 800": {
            "description": "shot on Kodak Portra 800 color negative film",
            "characteristics": "fine grain for high speed, natural colors, versatile lighting, warm color cast, professional quality"
        },
        "Fujifilm Pro 400H": {
            "description": "shot on Fujifilm Pro 400H color negative film",
            "characteristics": "muted pastels, soft cyan-green cast, delicate colors, smooth skin tones, dreamy aesthetic, wedding photography style"
        },
        "Kodak Ektar 100": {
            "description": "shot on Kodak Ektar 100 color negative film",
            "characteristics": "ultra vivid colors, high saturation, fine grain, punchy contrast, vibrant blues and greens, landscape quality"
        },
        "Fujifilm Superia 400": {
            "description": "shot on Fujifilm Superia 400 color negative film",
            "characteristics": "consumer film aesthetic, slightly warm tones, moderate saturation, nostalgic feel, everyday snapshot quality"
        },
        "Kodak Gold 200": {
            "description": "shot on Kodak Gold 200 color negative film",
            "characteristics": "warm golden tones, nostalgic color palette, consumer film look, soft contrast, sunny day aesthetic"
        },
        "Kodak ColorPlus 200": {
            "description": "shot on Kodak ColorPlus 200 color negative film",
            "characteristics": "budget film aesthetic, warm cast, moderate grain, vintage snapshot feel, 90s nostalgia"
        },
        
        # Color Slide/Reversal Films
        "Kodak Ektachrome E100": {
            "description": "shot on Kodak Ektachrome E100 color slide film",
            "characteristics": "vibrant saturated colors, fine grain, high contrast, rich blacks, punchy whites, professional quality, slide film aesthetic"
        },
        "Fujifilm Velvia 50": {
            "description": "shot on Fujifilm Velvia 50 color slide film",
            "characteristics": "extremely saturated colors, ultra fine grain, intense blues and greens, high contrast, landscape photography standard, vivid nature colors"
        },
        "Fujifilm Velvia 100": {
            "description": "shot on Fujifilm Velvia 100 color slide film",
            "characteristics": "highly saturated, vibrant colors, fine grain, rich tones, excellent detail, bold color palette"
        },
        "Fujifilm Provia 100F": {
            "description": "shot on Fujifilm Provia 100F color slide film",
            "characteristics": "neutral color balance, fine grain, accurate color reproduction, natural tones, professional standard"
        },
        "Kodachrome 64": {
            "description": "shot on Kodachrome 64 color slide film",
            "characteristics": "legendary color rendition, warm rich tones, subtle grain, iconic mid-century aesthetic, archival quality, National Geographic style"
        },
        
        # Instant Films
        "Polaroid SX-70": {
            "description": "shot on Polaroid SX-70 instant film",
            "characteristics": "soft dreamy colors, muted tones, square format, instant film aesthetic, vintage color cast, faded look, nostalgic feel"
        },
        "Polaroid 600": {
            "description": "shot on Polaroid 600 instant film",
            "characteristics": "classic instant photo look, slightly cool tones, soft focus, white border frame, retro aesthetic"
        },
        "Fujifilm Instax Wide": {
            "description": "shot on Fujifilm Instax Wide instant film",
            "characteristics": "modern instant film, bright colors, soft contrast, consumer aesthetic, party snapshot feel"
        },
        
        # Specialty & Vintage
        "Lomography Color Negative 400": {
            "description": "shot on Lomography Color Negative 400 film",
            "characteristics": "saturated colors, high contrast, experimental aesthetic, unpredictable color shifts, artistic grain"
        },
        "Cinestill 800T": {
            "description": "shot on Cinestill 800T tungsten film",
            "characteristics": "halation glow, neon light bloom, cinematic look, warm interior lighting, night photography aesthetic, urban glow"
        },
        "Cinestill 50D": {
            "description": "shot on Cinestill 50D daylight film",
            "characteristics": "cinematic color grading, fine grain, natural daylight balance, movie film aesthetic, rich color depth"
        },
        "Rollei Ortho 25": {
            "description": "shot on Rollei Ortho 25 orthochromatic film",
            "characteristics": "ultra fine grain, high contrast, infrared-like sky rendering, unique tonal response, vintage scientific aesthetic"
        }
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        """Define the input parameters for the node"""
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "portrait of a person",
                    "dynamicPrompts": False
                }),
            },
            "optional": {
                # Style strength (kept visible for quick access)
                "style_strength": (["subtle", "moderate", "strong"], {
                    "default": "moderate"
                }),
                
                # Enable/Disable switches for each category
                "enable_film": ("BOOLEAN", {
                    "default": True,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_lens": ("BOOLEAN", {
                    "default": True,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_lighting": ("BOOLEAN", {
                    "default": False,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_genre": ("BOOLEAN", {
                    "default": False,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_era": ("BOOLEAN", {
                    "default": False,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_process": ("BOOLEAN", {
                    "default": False,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "enable_photographer": ("BOOLEAN", {
                    "default": False,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                
                # Category selections (all optional now)
                "film_stock": (list(cls.FILM_STOCKS.keys()), {
                    "default": "Kodak Tri-X 400"
                }),
                "lens": (list(cls.LENSES.keys()), {
                    "default": "Nikkor 50mm f/1.4"
                }),
                "lighting_style": (list(cls.LIGHTING_STYLES.keys()), {
                    "default": "None (Natural)"
                }),
                "photography_genre": (list(cls.PHOTOGRAPHY_GENRES.keys()), {
                    "default": "None (General)"
                }),
                "photography_era": (list(cls.PHOTOGRAPHY_ERAS.keys()), {
                    "default": "None (Contemporary)"
                }),
                "technical_process": (list(cls.TECHNICAL_PROCESSES.keys()), {
                    "default": "None (Standard Processing)"
                }),
                "photographer_style": (list(cls.PHOTOGRAPHER_STYLES.keys()), {
                    "default": "None (Original Style)"
                }),
                
                # Global settings
                "add_technical_details": ("BOOLEAN", {
                    "default": True,
                    "label_on": "yes",
                    "label_off": "no"
                }),
                "custom_suffix": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("styled_prompt",)
    FUNCTION = "apply_film_style"
    CATEGORY = "conditioning/film_photography"
    OUTPUT_NODE = True  # This makes the node display its output
    
    def apply_film_style(self, prompt, style_strength, 
                         enable_film=True, enable_lens=True, enable_lighting=False,
                         enable_genre=False, enable_era=False, 
                         enable_process=False, enable_photographer=False,
                         film_stock=None, lens=None, lighting_style=None,
                         photography_genre=None, photography_era=None, 
                         technical_process=None, photographer_style=None,
                         add_technical_details=True, custom_suffix=""):
        """
        Apply comprehensive film photography style to the prompt
        
        Args:
            prompt: Original text prompt
            style_strength: How prominent the characteristics should be
            enable_film: Enable film stock characteristics
            enable_lens: Enable lens characteristics
            enable_lighting: Enable lighting style characteristics
            enable_genre: Enable photography genre characteristics
            enable_era: Enable photography era characteristics
            enable_process: Enable technical process characteristics
            enable_photographer: Enable photographer style characteristics
            film_stock: Selected film stock (if enabled)
            lens: Selected lens (if enabled)
            lighting_style: Selected lighting technique (if enabled)
            photography_genre: Selected genre (if enabled)
            photography_era: Selected photography era/movement (if enabled)
            technical_process: Selected darkroom/processing technique (if enabled)
            photographer_style: Selected photographer aesthetic (if enabled)
            add_technical_details: Whether to add detailed characteristics
            custom_suffix: Additional custom text to append
        
        Returns:
            Styled prompt with comprehensive film photography characteristics
        """
        
        # Set defaults if None
        if film_stock is None:
            film_stock = list(self.FILM_STOCKS.keys())[0]
        if lens is None:
            lens = "None (Film Only)"
        if lighting_style is None:
            lighting_style = "None (Natural)"
        if photography_genre is None:
            photography_genre = "None (General)"
        if photography_era is None:
            photography_era = "None (Contemporary)"
        if technical_process is None:
            technical_process = "None (Standard Processing)"
        if photographer_style is None:
            photographer_style = "None (Original Style)"
        
        # Get data for enabled categories
        film_data = self.FILM_STOCKS[film_stock] if enable_film else None
        lens_data = self.LENSES[lens] if enable_lens else None
        lighting_data = self.LIGHTING_STYLES[lighting_style] if enable_lighting else None
        genre_data = self.PHOTOGRAPHY_GENRES[photography_genre] if enable_genre else None
        era_data = self.PHOTOGRAPHY_ERAS[photography_era] if enable_era else None
        process_data = self.TECHNICAL_PROCESSES[technical_process] if enable_process else None
        photographer_data = self.PHOTOGRAPHER_STYLES[photographer_style] if enable_photographer else None
        
        # Start with the original prompt
        styled_prompt = prompt.strip()
        
        # Track if any photography elements were added
        added_elements = False
        
        # Add photographer style first (sets overall aesthetic if enabled)
        if enable_photographer and photographer_data and photographer_style != "None (Original Style)" and photographer_data['description']:
            styled_prompt += f", {photographer_data['description']}"
            added_elements = True
        
        # Add photography era context (sets historical period)
        if enable_era and era_data and photography_era != "None (Contemporary)" and era_data['description']:
            styled_prompt += f", {era_data['description']}"
            added_elements = True
        
        # Add genre (sets subject matter approach)
        if enable_genre and genre_data and photography_genre != "None (General)" and genre_data['description']:
            styled_prompt += f", {genre_data['description']}"
            added_elements = True
        
        # Add film stock description
        if enable_film and film_data and film_data['description']:
            styled_prompt += f", {film_data['description']}"
            added_elements = True
        
        # Add technical process (affects film look)
        if enable_process and process_data and technical_process != "None (Standard Processing)" and process_data['description']:
            styled_prompt += f", {process_data['description']}"
            added_elements = True
        
        # Add lens description if not "None"
        if enable_lens and lens_data and lens != "None (Film Only)" and lens_data['description']:
            styled_prompt += f", {lens_data['description']}"
            added_elements = True
        
        # Add lighting style
        if enable_lighting and lighting_data and lighting_style != "None (Natural)" and lighting_data['description']:
            styled_prompt += f", {lighting_data['description']}"
            added_elements = True
        
        # Add print style if not "None"
        
        # Add characteristics based on strength
        if add_technical_details:
            all_characteristics = []
            
            # Collect photographer style characteristics (foundational aesthetic)
            if enable_photographer and photographer_data and photographer_style != "None (Original Style)" and photographer_data['characteristics']:
                photographer_chars = photographer_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(photographer_chars[:min(5, len(photographer_chars))])
                elif style_strength == "moderate":
                    all_characteristics.extend(photographer_chars[:min(3, len(photographer_chars))])
                else:  # subtle
                    all_characteristics.extend(photographer_chars[:min(2, len(photographer_chars))])
            
            # Collect era characteristics
            if enable_era and era_data and photography_era != "None (Contemporary)" and era_data['characteristics']:
                era_chars = era_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(era_chars[:min(4, len(era_chars))])
                elif style_strength == "moderate":
                    all_characteristics.extend(era_chars[:min(2, len(era_chars))])
                else:  # subtle
                    all_characteristics.extend(era_chars[:min(1, len(era_chars))])
            
            # Collect genre characteristics
            if enable_genre and genre_data and photography_genre != "None (General)" and genre_data['characteristics']:
                genre_chars = genre_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(genre_chars[:min(4, len(genre_chars))])
                elif style_strength == "moderate":
                    all_characteristics.extend(genre_chars[:min(3, len(genre_chars))])
                else:  # subtle
                    all_characteristics.extend(genre_chars[:min(2, len(genre_chars))])
            
            # Collect film characteristics
            if enable_film and film_data and film_data['characteristics']:
                film_chars = film_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(film_chars)
                elif style_strength == "moderate":
                    all_characteristics.extend(film_chars[:min(4, len(film_chars))])
                else:  # subtle
                    all_characteristics.extend(film_chars[:min(2, len(film_chars))])
            
            # Collect technical process characteristics
            if enable_process and process_data and technical_process != "None (Standard Processing)" and process_data['characteristics']:
                process_chars = process_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(process_chars[:min(4, len(process_chars))])
                elif style_strength == "moderate":
                    all_characteristics.extend(process_chars[:min(3, len(process_chars))])
                else:  # subtle
                    all_characteristics.extend(process_chars[:min(2, len(process_chars))])
            
            # Collect lens characteristics
            if enable_lens and lens_data and lens != "None (Film Only)" and lens_data['characteristics']:
                lens_chars = lens_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(lens_chars)
                elif style_strength == "moderate":
                    all_characteristics.extend(lens_chars[:min(3, len(lens_chars))])
                else:  # subtle
                    all_characteristics.extend(lens_chars[:min(2, len(lens_chars))])
            
            # Collect lighting characteristics
            if enable_lighting and lighting_data and lighting_style != "None (Natural)" and lighting_data['characteristics']:
                lighting_chars = lighting_data['characteristics'].split(', ')
                if style_strength == "strong":
                    all_characteristics.extend(lighting_chars[:min(4, len(lighting_chars))])
                elif style_strength == "moderate":
                    all_characteristics.extend(lighting_chars[:min(3, len(lighting_chars))])
                else:  # subtle
                    all_characteristics.extend(lighting_chars[:min(2, len(lighting_chars))])
            
            # Collect print style characteristics
                    all_characteristics.extend(print_chars[:min(2, len(print_chars))])
            
            # Add all collected characteristics
            if all_characteristics:
                styled_prompt += f", {', '.join(all_characteristics)}"
                added_elements = True
        
        # Add general film photography terms only if any elements were added
        if added_elements:
            styled_prompt += ", analog photography"
            
            # Add era-appropriate terminology
            if enable_era and era_data and photography_era != "None (Contemporary)":
                era_desc = era_data.get('description', '')
                era_chars = era_data.get('characteristics', '')
                if "19th century" in era_desc or "1800s" in era_desc or "Victorian" in era_chars:
                    styled_prompt += ", vintage photography"
                elif "1900s" in era_desc or "1910s" in era_desc or "1920s" in era_desc:
                    styled_prompt += ", antique photography"
                else:
                    styled_prompt += ", film photography aesthetic"
            else:
                styled_prompt += ", film photography aesthetic"
        
        # Add custom suffix if provided
        if custom_suffix.strip():
            styled_prompt += f", {custom_suffix.strip()}"
        
        # Return the styled prompt and UI display information
        return {
            "ui": {"text": [styled_prompt]}, 
            "result": (styled_prompt,)
        }


# ComfyUI Node Registration
NODE_CLASS_MAPPINGS = {
    "FilmPromptStyler": FilmPromptStyler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilmPromptStyler": "Film Photography Prompt Styler"
}
