// ================================
// Resume File Upload
// ================================

const resumeFile = document.getElementById("resumeFile");
const filePreview = document.getElementById("filePreview");
const fileName = document.getElementById("fileName");
const fileSize = document.getElementById("fileSize");


// Check whether upload elements exist
if (resumeFile) {

    resumeFile.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) {
            return;
        }


        // Allowed file types
        const allowedExtensions = [
            ".pdf",
            ".doc",
            ".docx"
        ];

        const fileNameLower = file.name.toLowerCase();

        const isValidFile = allowedExtensions.some(function (extension) {
            return fileNameLower.endsWith(extension);
        });


        // Invalid file type
        if (!isValidFile) {

            alert("Please upload a PDF, DOC, or DOCX file.");

            resumeFile.value = "";

            if (filePreview) {
                filePreview.style.display = "none";
            }

            return;
        }


        // Maximum file size = 5 MB
        const maxSize = 5 * 1024 * 1024;

        if (file.size > maxSize) {

            alert("File size must be less than 5 MB.");

            resumeFile.value = "";

            if (filePreview) {
                filePreview.style.display = "none";
            }

            return;
        }


        // Display selected file
        if (fileName) {
            fileName.textContent = file.name;
        }


        if (fileSize) {

            const sizeInMB =
                (file.size / (1024 * 1024)).toFixed(2);

            fileSize.textContent =
                sizeInMB + " MB";
        }


        if (filePreview) {
            filePreview.style.display = "flex";
        }

    });

}


// ================================
// Remove Selected File
// ================================

function removeFile() {

    if (resumeFile) {
        resumeFile.value = "";
    }

    if (filePreview) {
        filePreview.style.display = "none";
    }

}


// ================================
// Analyze Resume
// ================================

function analyzeResume() {

    if (!resumeFile || !resumeFile.files.length) {

        alert("Please select your resume first.");

        return;
    }


    const file = resumeFile.files[0];

    console.log("Resume selected:", file.name);


    /*
        BACKEND CONNECTION WILL BE ADDED LATER.

        Final flow:

        Resume File
             ↓
        Flask Backend
             ↓
        PDF/DOCX Text Extraction
             ↓
        NLP Skill Extraction
             ↓
        Resume Analysis
             ↓
        Skill Gap Analysis
             ↓
        Career Recommendation
    */


    alert(
        "Resume selected successfully. " +
        "AI analysis will be connected with the Flask backend next."
    );

}
