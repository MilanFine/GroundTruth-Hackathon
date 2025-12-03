import React from 'react';

const ResultsGallery = ({ results, onDownload }) => {
    if (!results) return null;

    return (
        <div className="results-container">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '3rem' }}>
                <h2>Generated Variations</h2>
                <button className="btn-primary" style={{ width: 'auto', marginTop: 0 }} onClick={onDownload}>
                    Download All (ZIP)
                </button>
            </div>

            <div className="gallery-grid">
                {results.images.map((imgUrl, index) => (
                    <div key={index} className="glass-card creative-card">
                        <img src={imgUrl} alt={`Variation ${index + 1}`} className="creative-image" />
                        <p className="creative-caption">
                            {results.captions[index % results.captions.length]}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ResultsGallery;
