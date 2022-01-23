import NotesAPI from "./noteApi.js";
import noteApi from "./noteApi.js";

noteApi.saveNote({
    title: "New Note!",
    body: "I am a new note."
});

console.log(noteApi.getAllNotes());