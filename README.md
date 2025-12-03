# Auto-Creative Engine

The Auto-Creative Engine is a powerful tool designed to automate the creation of marketing assets. By uploading a brand logo and a product image, the engine generates multiple high-quality ad creative variations using Generative AI.

## Features

- **Automated Variation Generation**: Generates 10+ unique ad creatives.
- **AI-Powered Copy**: Generates compelling ad copy and captions using LLMs.
- **Premium UI**: A modern, responsive interface with glassmorphism design.
- **One-Click Download**: Download all generated assets in a single ZIP file.

## Tech Stack

- **Backend**: Python, FastAPI
- **Frontend**: React, Vite, Vanilla CSS
- **AI Integration**: OpenAI (DALL-E 3, GPT-4) 

## Setup & Installation

### Prerequisites

- Node.js (v18+)
- Python (v3.8+)

### Backend Setup

1. Navigate to the root directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Run the server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`.

## Usage

1. Open the web app.
2. Upload your Brand Logo and Product Image.
3. Enter a product description.
4. Click "Generate Auto-Creatives".
5. View the generated variations in the gallery.
6. Click "Download All (ZIP)" to save the assets.
