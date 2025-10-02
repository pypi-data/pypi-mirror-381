# 🧵 erabytse-veil  
*An ethical veil for image metadata — not deletion, but intentional protection.*

> "Not all metadata should be hidden. But what is sensitive deserves a veil."

## 🌿 Philosophy
- **GPS, timestamps, device IDs** → veiled (privacy risk)  
- **Aperture, focal length, lens** → preserved (creative value)  
- Every image is treated with **discernment, not fear**.

## ✨ Features (v0.1)
- Removes sensitive EXIF (GPS, precise timestamps, device IDs)  
- Preserves creative EXIF (f-stop, ISO, focal length)  
- Generates a clean output file — original untouched  
- **100% offline, no cloud, no tracking**

## 🚀 Quick Start

pip install -e .
erabytse-veil --input photo.jpg --output photo_veiled.jpg

📜 License
MIT — used with intention.

Part of erabytse — a quiet rebellion against digital waste.