# ChatSnake 🐍🎮

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey)]()

**ChatSnake** is a desktop Python game combining the classic Snake gameplay with an **interactive AI-powered chat companion**. The AI reacts in real-time to your actions, providing witty, sarcastic, friendly, or dramatic commentary. The game also features **sounds and offline TTS (Text-to-Speech)** for immersive gameplay.

---

## ✨ Features

- 🎮 **Classic Snake Gameplay** — Navigate, grow, and survive with increasing difficulty
- 🤖 **AI Chat Companion** — Reacts in real-time to:
  - Game start events
  - Eating food
  - Score milestones (every 5 points)
  - Crashing and game over
  - Pausing / Resuming
- 😄 **Multiple Personalities** — Choose from:
  - 😏 Sarcastic
  - 😊 Friendly
  - 🎭 Dramatic
- 🔊 **Text-to-Speech (TTS)** — Offline AI voice via `pyttsx3`
- 🎵 **Sound Effects** — Eat and crash sounds (`.mp3` or `.wav` fallback)
- 💬 **Dynamic Chat Panel** — AI responses displayed beside the game area
- ⌨️ **Responsive Controls**:
  - **Arrow Keys / WASD** → Move snake
  - **P** → Pause / Resume
  - **R** → Restart after game over

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ChatSnake.git
cd ChatSnake
```

### Step 2: Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: (Optional) Add API Key for Gemini
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```
Without this, the game uses fallback canned AI responses.

---

## 🚀 Running the Game

```bash
python main.py
```

The game window will open with:
- Snake gameplay on the left
- AI chat panel on the right
- AI greets you asynchronously
- Real-time commentary as you play

Sounds and TTS will play automatically if supported on your system.

---

## 📦 Packaging as Executable (Windows)

Create a standalone `.exe` file for distribution:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "assets;assets" main.py
```

The executable will be generated in the `dist/` folder. Include the `assets` folder with your executable so sounds work correctly.

---

## 📋 Dependencies

| Package | Purpose |
|---------|---------|
| **pygame** | Game graphics, rendering, and audio |
| **pyttsx3** | Offline Text-to-Speech |
| **requests** | HTTP requests for Gemini API (optional) |
| **python-dotenv** | Load environment variables from `.env` |
| **textwrap** | Text wrapping for chat display |

See `requirements.txt` for exact versions.

---

## 📁 Project Structure

```
ChatSnake/
│
├─ main.py                 # Entry point for the game
├─ snake_game.py           # Game logic and AI integration
├─ ai_chat.py              # AI chat class with Gemini API & TTS
├─ personalities.py        # AI personality templates and responses
├─ utils.py                # Helper functions for text rendering
│
├─ assets/                 # Sounds and other game assets
│  ├─ eat_sound.mp3
│  └─ crash_sound.mp3
│
├─ requirements.txt        # Python dependencies
├─ .env                    # API keys (not tracked in Git)
├─ .gitignore              # Git ignore rules
├─ LICENSE                 # MIT License
└─ README.md               # This file
```

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| **↑ ↓ ← →** | Move snake (Arrow Keys) |
| **W A S D** | Move snake (WASD) |
| **P** | Pause / Resume game |
| **R** | Restart after game over |

---

## 🎮 Gameplay Tips

- 🎯 **Collect food** to grow your snake and increase your score
- ⚠️ **Avoid walls** — Hitting boundaries ends the game
- 🐍 **Don't collide** with your own tail
- 📈 **Reach milestones** to unlock AI personality reactions
- 🎧 **Enable sound** for the full immersive experience

---

## 🔧 Configuration

### Changing AI Personality
Edit `personalities.py` to modify AI responses or add new personalities:

```python
PERSONALITIES = {
    "sarcastic": {
        "start": "Oh great, another snake game. How original.",
        "eat": "Wow, you ate something. Shocking.",
        # ... more responses
    },
    # Add your own personality here
}
```

### Using Gemini API
Set your `GEMINI_API_KEY` in `.env` for dynamic AI responses. Without it, the game uses predefined responses.

---

## ⚙️ System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8+
- **RAM**: 256 MB minimum
- **Display**: 1024x768 minimum resolution
- **Sound**: Optional (game works without audio)

---

## 🐛 Troubleshooting

**Q: No sound is playing**
- Ensure `assets/` folder is in the same directory as `main.py`
- Check if audio files are in `.mp3` or `.wav` format
- Verify your system audio is not muted

**Q: TTS is not working**
- Install `pyttsx3`: `pip install pyttsx3`
- Check if your OS supports TTS (all major OS do)
- Try `pyttsx3 --test-speak` to verify installation

**Q: Game is running slowly**
- Close background applications
- Reduce screen resolution
- Check Python version (use 3.8+)

**Q: API key errors**
- Verify `GEMINI_API_KEY` is correctly set in `.env`
- Check internet connection for online AI responses
- Without API key, canned responses will be used

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License © 2025 Vinayak Joshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🎯 Roadmap

- [ ] **Web version** (React/Canvas port)
- [ ] **Leaderboard** with score persistence
- [ ] **Custom themes** for snake and board
- [ ] **Difficulty levels** (Easy, Medium, Hard)
- [ ] **Multiplayer mode** (local co-op)
- [ ] **Mobile version** (Pygame Mobile)

---

## 💡 Future Ideas

- 🌈 Customizable color themes
- 🎵 Background music selection
- 🏆 Achievement system
- 🎮 Power-ups (speed boost, invincibility)
- 👥 Local multiplayer snake battles

---

## 📧 Contact & Support

For issues, questions, or suggestions:
- **GitHub Issues**: [Open an issue](https://github.com/yourusername/ChatSnake/issues)
- **Email**: vinayakjoshi2004@gmail.com

---

## 🙏 Acknowledgments

- **Pygame** community for excellent game development framework
- **pyttsx3** for offline text-to-speech
- **Google Gemini API** for AI-powered responses
- All contributors and testers

---

**Happy gaming! 🐍🎮 May your snake grow long and your AI commentary be entertaining!**