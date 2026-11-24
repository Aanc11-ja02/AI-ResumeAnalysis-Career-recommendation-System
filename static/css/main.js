/**
 * ResumeAI - Client-side Interactive Behaviors
 */

document.addEventListener('DOMContentLoaded', function () {
    initResumeUpload();
    initAutoDismissAlerts();
});

/**
 * Handles Drag-and-Drop, File Validation, and Processing Modal
 */
function initResumeUpload() {
    const fileInput = document.getElementById('resumeFileInput');
    const dropzone = document.getElementById('dropzone');
    const uploadIdle = document.getElementById('uploadIdle');
    const uploadSelected = document.getElementById('uploadSelected');
    const selectedFileName = document.getElementById('selectedFileName');
    const selectedFileSize = document.getElementById('selectedFileSize');
    const removeFileBtn = document.getElementById('removeFileBtn');
    const submitBtn = document.getElementById('submitBtn');
    const fileErrorAlert = document.getElementById('fileErrorAlert');
    const fileErrorMessage = document.getElementById('fileErrorMessage');
    const uploadForm = document.getElementById('resumeUploadForm');

    if (!fileInput || !dropzone) return;

    const MAX_SIZE_BYTES = 5 * 1024 * 1024; // 5 MB
    const ALLOWED_EXTENSIONS = ['pdf', 'docx'];

    function showError(msg) {
        if (fileErrorAlert && fileErrorMessage) {
            fileErrorMessage.textContent = msg;
            fileErrorAlert.classList.remove('d-none');
        }
        if (submitBtn) submitBtn.disabled = true;
    }

    function clearError() {
        if (fileErrorAlert) {
            fileErrorAlert.classList.add('d-none');
        }
    }

    function formatBytes(bytes) {
        if (bytes < 1024) return bytes + ' B';
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
    }

    function validateAndDisplayFile(file) {
        clearError();

        if (!file) {
            resetUploadUI();
            return false;
        }

        const ext = file.name.split('.').pop().toLowerCase();
        if (!ALLOWED_EXTENSIONS.includes(ext)) {
            showError(`Unsupported file format (.${ext}). Only PDF and DOCX documents are accepted.`);
            resetUploadUI();
            return false;
        }

        if (file.size > MAX_SIZE_BYTES) {
            showError(`File size (${formatBytes(file.size)}) exceeds the maximum allowed limit of 5 MB.`);
            resetUploadUI();
            return false;
        }

        // Valid file
        if (selectedFileName) selectedFileName.textContent = file.name;
        if (selectedFileSize) selectedFileSize.textContent = formatBytes(file.size);
        if (uploadIdle) uploadIdle.classList.add('d-none');
        if (uploadSelected) uploadSelected.classList.remove('d-none');
        if (submitBtn) submitBtn.disabled = false;

        return true;
    }

    function resetUploadUI() {
        if (fileInput) fileInput.value = '';
        if (uploadIdle) uploadIdle.classList.remove('d-none');
        if (uploadSelected) uploadSelected.classList.add('d-none');
        if (submitBtn) submitBtn.disabled = true;
    }

    // Input change
    fileInput.addEventListener('change', function () {
        if (fileInput.files && fileInput.files[0]) {
            validateAndDisplayFile(fileInput.files[0]);
        }
    });

    // Drag and drop listeners
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, function (e) {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, function (e) {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dragover');
        });
    });

    dropzone.addEventListener('drop', function (e) {
        const dt = e.dataTransfer;
        if (dt && dt.files && dt.files.length > 0) {
            const file = dt.files[0];
            fileInput.files = dt.files;
            validateAndDisplayFile(file);
        }
    });

    // Remove file button
    if (removeFileBtn) {
        removeFileBtn.addEventListener('click', function (e) {
            e.preventDefault();
            clearError();
            resetUploadUI();
        });
    }

    // Processing modal on submit
    if (uploadForm) {
        uploadForm.addEventListener('submit', function (e) {
            if (!fileInput.files || fileInput.files.length === 0) {
                e.preventDefault();
                showError('Please choose a file before submitting.');
                return;
            }

            const modalEl = document.getElementById('processingModal');
            if (modalEl && typeof bootstrap !== 'undefined') {
                const modal = new bootstrap.Modal(modalEl);
                modal.show();

                const progressBar = document.getElementById('processingProgressBar');
                const statusText = document.getElementById('processingStatusText');
                const step1 = document.getElementById('step1');
                const step2 = document.getElementById('step2');
                const step3 = document.getElementById('step3');
                const step4 = document.getElementById('step4');

                // Staged progress indication
                let progress = 20;
                const interval = setInterval(() => {
                    progress += 15;
                    if (progress <= 90 && progressBar) {
                        progressBar.style.width = progress + '%';
                    }

                    if (progress === 35) {
                        if (statusText) statusText.textContent = 'Extracting hard & soft skills with spaCy NLP...';
                        if (step2) step2.classList.add('fw-bold', 'text-primary');
                    } else if (progress === 55) {
                        if (statusText) statusText.textContent = 'Predicting experience tier with Random Forest Classifier...';
                        if (step3) step3.classList.add('fw-bold', 'text-primary');
                    } else if (progress === 75) {
                        if (statusText) statusText.textContent = 'Evaluating semantic similarity with Sentence-Transformers...';
                        if (step4) step4.classList.add('fw-bold', 'text-primary');
                    } else if (progress >= 95) {
                        clearInterval(interval);
                    }
                }, 750);
            }
        });
    }
}

/**
 * Automatically dismisses flash messages after 6 seconds
 */
function initAutoDismissAlerts() {
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 7000);
    });
}
