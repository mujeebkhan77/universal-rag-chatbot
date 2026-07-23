function DocumentList({ documents, handleDelete }) {


  return (
    <div>

      <h2 className="text-sm font-semibold text-gray-500 uppercase mb-4">
        Documents
      </h2>


      <div className="space-y-3">

        {documents.map((doc, index) => (
          <div
            key={index}
            className="
              flex items-center gap-3
              border border-gray-200
              rounded-xl
              p-3
              bg-white
              hover:bg-gray-50
              hover:shadow-sm
              transition-all
              cursor-pointer
            "
          >

            <div className="text-xl">
              {doc.type === "youtube" ? "🎥" : "📄"}
            </div>


            <div>
              <p className="text-sm font-medium text-gray-800">
                {doc.name}
              </p>

              <p className="text-xs text-gray-500">
                {doc.type === "youtube"
                  ? "Youtube Source"
                  : "PDF Document"}
              </p>
            </div>

            <button
              onClick={() => handleDelete(doc.document_id)}
              className="ml-auto text-red-500 hover:text-red-700"
            >
              🗑
            </button>
          </div>
        ))}

      </div>

    </div>
  );
}

export default DocumentList;