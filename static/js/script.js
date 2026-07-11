document.addEventListener('DOMContentLoaded', () => {
    const uploadZone = document.getElementById('upload-zone');
    const fileInput = document.getElementById('file-input');
    const previewImg = document.getElementById('image-preview');
    const uploadPrompt = document.getElementById('upload-prompt');
    const generateBtn = document.getElementById('generate-btn');
    const loader = document.getElementById('loader');
    const resultArea = document.getElementById('result-area');
    const captionText = document.getElementById('caption-text');

    uploadZone.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                previewImg.src = e.target.result;
                previewImg.style.display = 'block';
                uploadPrompt.style.display = 'none';
                generateBtn.style.display = 'inline-block';
                resultArea.style.display = 'none';
            }
            reader.readAsDataURL(file);
        }
    });

    generateBtn.addEventListener('click', async () => {
        const file = fileInput.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('image', file);

        // UI Transition
        generateBtn.style.display = 'none';
        loader.style.display = 'block';
        resultArea.style.display = 'none';

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();

            if (data.success) {
                captionText.innerText = data.caption;
                resultArea.style.display = 'block';
            } else {
                alert("Generation failed: " + data.error);
                generateBtn.style.display = 'inline-block';
            }
        } catch (error) {
            alert("Error connecting to server.");
            generateBtn.style.display = 'inline-block';
        } finally {
            loader.style.display = 'none';
        }
    });
});