**#** 🧠 AI Developer Challenge – Prompt to 3D Model Generator****

This is an intelligent end-to-end AI application that transforms simple text prompts into stunning 3D models using a local LLM and Openfabric AI services. It supports prompt memory, a Streamlit GUI, and Docker deployment.

---

## 🚀 Features

- ✨ Local LLM prompt expansion (mocked)
- 🖼️ Image generation using Openfabric Text-to-Image app
- 🧊 3D model generation using Openfabric Image-to-3D app
- 🧠 Prompt memory with SQLite database
- 🖥️ GUI with Streamlit
- 🐳 Docker support

---

## 🔄 Workflow

**User Prompt**  
⬇️  
**Expanded Prompt (LLM)**  
⬇️  
**Image Generation via Openfabric**  
⬇️  
**3D Model Generation via Openfabric**  
⬇️  
**Stored in Memory (SQLite)**

---

## 💻 How to Run

### 🧪 Run Locally

```bash
pip install streamlit
streamlit run app_gui.py


---

## 🧠 Memory System

All prompts and their expanded versions are stored in a local SQLite database called `memory.db`. This allows the app to remember what you generated earlier.

Example:
```python
from utils.memory import retrieve_from_memory
print(retrieve_from_memory("Design a spaceship"))
📂 Project Structure
bash
Copy
Edit
ai-dev-challenge1/
├── main.py                 # Core logic for generation
├── app_gui.py              # Streamlit frontend
├── utils/                  # Helper modules
│   ├── llm_utils.py
│   ├── openfabric_stub.py
│   ├── memory.py
│   └── schemas.py
├── assets/                 # Output files (image, model)
│   ├── generated.png
│   └── model.glb
├── memory.db               # SQLite database
├── Dockerfile
└── start.sh
🎨 Sample Prompt
Prompt: "Design a futuristic city with floating cars"
Expanded: A highly detailed futuristic skyline with flying cars, glowing towers, and neon-lit roads
Outputs:

assets/generated.png

assets/model.glb

📦 Tech Stack
Python 3.10

Openfabric SDK (Stub simulation)

SQLite

Streamlit

Docker

👨‍💻 Developed By
Balaji Reddy
This project was built as part of the AI Developer Challenge.

📨 Feedback
Have suggestions or questions?
Open an issue → https://github.com/Balaji7095/ai-dev-challenge1/issues

yaml
Copy
Edit










