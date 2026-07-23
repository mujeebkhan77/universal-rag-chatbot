import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import { useState, useEffect } from "react";
import axios from "axios";
import client from "./api/client";

function App() {
  const [messages, setMessages] = useState([]);
  const [documents, setDocuments] = useState([]);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [loading, setLoading] = useState(false);


  const fetchDocuments = async () => {
    try {
      const response = await client.get("/documents");
      console.log(response.data);
      setDocuments(response.data);
    } catch (error) {
      console.error(error);
    }
  };


  useEffect(() => {
    fetchDocuments();
  }, []);


  const addMessage = (newMessage) => {
    setMessages((prevMessages) => [
      ...prevMessages,
      newMessage
    ]);
  };

  const handleSend = async (question) => {

    addMessage({
      role: "user",
      content: question,
      sources: []
    });

    setLoading(true);

    try {

      const response = await client.post("/chat", {
        question: question
      });

      addMessage({
        role: "assistant",
        content: response.data.answer,
        sources: response.data.sources
      });

    } catch (error) {

      addMessage({
        role: "assistant",
        content: "Sorry, something went wrong. Please try again.",
        sources: []
      });

    } finally {

      setLoading(false);

    }

  };

  const handleDelete = async (document_id) => {
    try {
      await client.delete(`/documents/${document_id}`);

      setDocuments((prevDocuments) =>
        prevDocuments.filter(
          (doc) => doc.document_id !== document_id
        )
      );

    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="h-screen flex">
      <Sidebar
        sidebarOpen={sidebarOpen}
        setSidebarOpen={setSidebarOpen}
        documents={documents}
        fetchDocuments={fetchDocuments}
        handleDelete={handleDelete}
      />
      <ChatWindow
        messages={messages}
        addMessage={addMessage}
        handleSend={handleSend}
        loading={loading}
      />
    </div>
  );
}

export default App;