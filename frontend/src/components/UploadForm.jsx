import React, { useState, useRef } from 'react';

const UploadForm = ({ onGenerate, isLoading }) => {
  const [logo, setLogo] = useState(null);
  const [productImage, setProductImage] = useState(null);
  const [description, setDescription] = useState('');
  const [dragActive, setDragActive] = useState(false);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      // Handle file drop logic (simplified for demo to just pick the first file as product image if not set)
      if (!productImage) setProductImage(e.dataTransfer.files[0]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (logo && productImage && description) {
      onGenerate(logo, productImage, description);
    } else {
      alert("Please fill in all fields");
    }
  };

  return (
    <form className="glass-card" onSubmit={handleSubmit} onDragEnter={handleDrag}>
      <div className="upload-container" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        
        {/* Logo Upload */}
        <div className={`upload-area ${dragActive ? 'drag-active' : ''}`}>
          <label className="upload-label">
            <span className="icon">🎨</span>
            <span>{logo ? logo.name : "Upload Brand Logo"}</span>
            <input 
              type="file" 
              accept="image/*" 
              onChange={(e) => setLogo(e.target.files[0])} 
            />
          </label>
        </div>

        {/* Product Image Upload */}
        <div className={`upload-area ${dragActive ? 'drag-active' : ''}`}>
          <label className="upload-label">
            <span className="icon">📸</span>
            <span>{productImage ? productImage.name : "Upload Product Image"}</span>
            <input 
              type="file" 
              accept="image/*" 
              onChange={(e) => setProductImage(e.target.files[0])} 
            />
          </label>
        </div>
      </div>

      <textarea
        placeholder="Describe your product and target audience..."
        rows="4"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button type="submit" className="btn-primary" disabled={isLoading}>
        {isLoading ? "Generating Magic..." : "Generate Auto-Creatives"}
      </button>
    </form>
  );
};

export default UploadForm;
