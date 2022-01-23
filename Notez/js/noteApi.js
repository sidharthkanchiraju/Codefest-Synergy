export default class noteApi {
    static getAllNotes(){
        const notes = JSON.parse(JSON.stringify(localStorage.getItem("notesapp-notes")) || "[]");

        return notes.sort((a,b) =>{
            return new Date(a.updated) > new Date(b.updated) ? -1 : 1;
        });

    }
    static saveNote(noteToSave){
        const notes = noteAPI.getAllNotes();

        noteToSave.id = Math.floor(Math.random() * 1000000);
        noteToSave.updated = new Date().toISOString();  
        notes.push(noteToSave);

        localStorage.setItem("notesapp-notes", JSON.stringify(notes));
    }
    static deleteNote(id){

    }
}