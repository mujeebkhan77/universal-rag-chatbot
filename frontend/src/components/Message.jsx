import { User, Bot } from "lucide-react";

function Message({ role, content, sources }) {
  const isUser = role === "user";

  return (
    <div
      className={`mb-5 flex gap-3 items-start ${isUser ? "justify-end" : "justify-start"
        }`}
    >

      {/* AI Avatar */}
      {!isUser && (
        <div className="bg-gray-200 p-2 rounded-full h-fit">
          <Bot size={18} />
        </div>
      )}


      {/* Message Bubble */}
      <div
        className={`max-w-3xl px-5 py-4 rounded-2xl shadow-sm transition-all duration-200 ${isUser
            ? "bg-blue-600 text-white rounded-br-md"
            : "bg-white border border-gray-200 text-gray-900 rounded-bl-md"
          }`}
      >

        <p
          className={`text-xs font-semibold uppercase tracking-wide mb-2 ${isUser ? "text-blue-100" : "text-gray-500"
            }`}
        >
          {isUser ? "You" : "AI"}
        </p>


        <p className="leading-7 whitespace-pre-wrap">
          {content}
        </p>


        {sources && sources.length > 0 && (
          <div className="mt-4 pt-3 border-t border-gray-200">

            <p className="text-sm font-semibold mb-2">
              Sources
            </p>


            <div className="space-y-2">

              {sources.map((source, index) => (
                <div
                  key={index}
                  className="bg-gray-50 border border-gray-200 rounded-lg px-3 py-2 text-sm"
                >
                  {source.source === "youtube" ? (
                    <>
                      🎥 {source.video_id}
                    </>
                  ) : (
                    <>
                      📄 {source.file}
                      {source.page && ` • Page ${source.page}`}
                    </>
                  )}
                </div>
              ))}

            </div>

          </div>
        )}

      </div>


      {/* User Avatar */}
      {isUser && (
        <div className="bg-blue-600 text-white p-2 rounded-full h-fit">
          <User size={18} />
        </div>
      )}

    </div>
  );
}

export default Message;