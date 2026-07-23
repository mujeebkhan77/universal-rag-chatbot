import { Sparkles } from "lucide-react";

function Header() {
  return (
    <div className="h-16 border-b bg-white flex items-center justify-between px-6">

      <div className="flex items-center gap-3">

        <div className="bg-blue-600 text-white p-2 rounded-xl">
          <Sparkles size={20} />
        </div>


        <div>
          <h1 className="text-lg font-semibold text-gray-800">
            Universal RAG
          </h1>

          <p className="text-xs text-gray-500">
            AI document assistant
          </p>
        </div>

      </div>


      <div className="flex items-center gap-2 text-sm text-gray-500">

        <span className="w-2 h-2 bg-green-500 rounded-full"></span>

        Gemini Flash

      </div>


    </div>
  );
}

export default Header;