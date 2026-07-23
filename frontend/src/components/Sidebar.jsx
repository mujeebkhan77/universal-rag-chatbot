import { useState, useRef } from "react";

import client from "../api/client";

import DocumentList from "./DocumentList";


function Sidebar({
  sidebarOpen,
  setSidebarOpen,
  documents,
  fetchDocuments,
  handleDelete
}) {

  const [uploading, setUploading] = useState(false);
  const [uploadMessage, setUploadMessage] = useState("");
  const fileInputRef = useRef(null);
  const [youtubeUrl, setYoutubeUrl] = useState("");
  const [showYoutubeInput, setShowYoutubeInput] = useState(false);
  const [youtubeLoading, setYoutubeLoading] = useState(false);

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };


  const handleFileChange = async (event) => {
    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {

      setUploading(true);

      const response = await client.post("/ingest/file", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });


      await fetchDocuments();
      event.target.value = "";


      setUploadMessage(response.data.message);

      setTimeout(() => {
        setUploadMessage("");
      }, 3000);


    } catch (error) {

      console.error(error);
      alert("Upload failed.");

    } finally {

      setUploading(false);

    }
  };

  const handleYoutubeSubmit = async () => {

    if (!youtubeUrl) return;

    try {

      setYoutubeLoading(true);

      const response = await client.post("/ingest/youtube", {
        url: youtubeUrl
      });

      await fetchDocuments();

      setUploadMessage(response.data.message);

      setYoutubeUrl("");

      setShowYoutubeInput(false);

      setTimeout(() => {
        setUploadMessage("");
      }, 3000);


    } catch (error) {

      console.error(error);
      alert("YouTube upload failed.");

    } finally {

      setYoutubeLoading(false);

    }

  };

  return (
    <aside
      className={`
       ${sidebarOpen ? "w-80 p-6" : "w-16 p-3"}
       border-r bg-white flex flex-col
       transition-all duration-300
       overflow-hidden
      `}
    >

      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className={`
          mb-4
          text-gray-600
          hover:text-black
          transition
          ${sidebarOpen ? "self-start" : "self-center"}
        `}
      >
        ☰
      </button>


      {/* Logo / Title */}

      {sidebarOpen && (
        <div className="mb-8">

          <h1 className="text-2xl font-bold text-gray-900">
            Universal RAG
          </h1>

          <p className="text-sm text-gray-500 mt-1">
            Chat with your documents
          </p>

        </div>
      )}



      {/* Actions */}

      {sidebarOpen && (
        <div className="space-y-3">


          <button
            onClick={handleUploadClick}
            className="
              w-full 
              bg-blue-600 
              hover:bg-blue-700
              transition
              text-white 
              py-3 
              rounded-xl
              font-medium
            "
          >
            {uploading ? "Uploading..." : "Upload Document"}
          </button>


          {uploadMessage && (
            <p className="text-sm text-green-600 mt-2">
              {uploadMessage}
            </p>
          )}


          <input
            type="file"
            accept=".pdf,.docx,.txt"
            ref={fileInputRef}
            onChange={handleFileChange}
            className="hidden"
          />



          <button
            onClick={() => setShowYoutubeInput(!showYoutubeInput)}
            className="
              w-full 
              bg-gray-900
              hover:bg-gray-800
              transition
              text-white 
              py-3 
              rounded-xl
              font-medium
            "
          >
            Add YouTube URL
          </button>

          {showYoutubeInput && (
            <div className="space-y-2">

              <input
                type="text"
                placeholder="Paste YouTube URL"
                value={youtubeUrl}
                onChange={(e) => setYoutubeUrl(e.target.value)}
                className="
                  w-full
                  border
                  rounded-xl
                  p-3
                  text-sm
               "
              />


              <button
                onClick={handleYoutubeSubmit}
                className="
                w-full
                bg-red-600
                hover:bg-red-700
                text-white
                py-2
                rounded-xl
              "
              >
                {youtubeLoading ? "Processing..." : "Add Video"}
              </button>

            </div>
          )}

        </div>
      )}



      {/* Documents */}

      {sidebarOpen && (
        <div className="mt-8 flex-1 overflow-y-auto">

          <DocumentList
            documents={documents}
            handleDelete={handleDelete}
          />

        </div>
      )}


    </aside>
  );
}


export default Sidebar;