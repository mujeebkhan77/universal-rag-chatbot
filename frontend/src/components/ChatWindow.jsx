import InputBox from "./InputBox";
import Message from "./Message";
import { useEffect, useRef } from "react";
import Header from "./Header";

function ChatWindow({ messages, addMessage, handleSend, loading }) {

    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages]);

    return (
        <div className="flex-1 flex flex-col bg-gray-50">

            <Header />
            
            <div className="flex-1 overflow-y-auto px-6 py-6">
                {messages.length === 0 && (
                    <div className="h-full flex flex-col items-center justify-center text-center">

                        <h1 className="text-3xl font-bold text-gray-800">
                            ✨ Universal RAG
                        </h1>

                        <p className="mt-3 text-gray-500">
                            Chat with your documents and YouTube sources
                        </p>

                        <p className="mt-2 text-sm text-gray-400">
                            Upload a source and ask anything
                        </p>

                    </div>
                )}

                {messages.map((message, index) => (
                    <Message
                        key={index}
                        role={message.role}
                        content={message.content}
                        sources={message.sources}
                    />
                ))}

                {loading && (
                    <div className="mb-4 text-left">

                        <div className="inline-block bg-gray-100 px-4 py-3 rounded-xl">

                            <p className="text-sm font-semibold mb-2">
                                AI
                            </p>

                            <div className="flex gap-1">
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:150ms]"></span>
                                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:300ms]"></span>
                            </div>

                        </div>

                    </div>
                )}

                <div ref={messagesEndRef}></div>
            </div>


            <div className="border-t bg-white px-6 py-4">
                <InputBox onSend={handleSend} />
            </div>

        </div>
    );
}

export default ChatWindow;