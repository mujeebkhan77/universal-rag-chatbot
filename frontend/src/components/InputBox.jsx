import { useState } from "react";

function InputBox({ onSend }) {
    const [question, setQuestion] = useState("");

    const handleSend = () => {
        if (!question.trim()) return;

        onSend(question);
        setQuestion("");
    };

    return (
        <div className="flex items-end gap-3 bg-white border border-gray-200 rounded-2xl shadow-sm px-4 py-3">

            <textarea
                rows={1}
                value={question}
                placeholder="Ask anything about your sources..."
                onChange={(e) => setQuestion(e.target.value)}
                onInput={(e) => {
                    e.target.style.height = "auto";
                    e.target.style.height = `${e.target.scrollHeight}px`;
                }}
                onKeyDown={(e) => {
                    if (e.key === "Enter" && !e.shiftKey) {
                        e.preventDefault();
                        handleSend();
                    }
                }}
                className="flex-1 resize-none overflow-hidden bg-transparent outline-none text-gray-800 placeholder-gray-400 leading-6 max-h-40"
            />

            <button
                onClick={handleSend}
                disabled={!question.trim()}
                className={`flex h-11 w-11 items-center justify-center rounded-xl text-white transition-all duration-200 ${question.trim()
                        ? "bg-blue-600 hover:bg-blue-700 hover:scale-105"
                        : "bg-gray-300 cursor-not-allowed"
                    }`}
            >
                ➤
            </button>

        </div>
    );
}

export default InputBox;