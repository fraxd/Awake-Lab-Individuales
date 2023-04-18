const form = document.querySelector('form');
const commentList = document.getElementById('comment-list');


// Agregar al listado
function agregarComentario(event){
    event.preventDefault(); // prevenir el comportamiento predeterminado del formulario
    const commentInput = document.getElementById('comment');
    const comment = commentInput.value.trim();

    if (comment !== '') {
        console.log('Agregado al listado')
        const li = document.createElement('li');
        li.textContent = comment;
        commentList.appendChild(li);
        commentInput.value = '';
    }
}


//Eliminar del listado
function eliminarComentario(event){
    if (event.target.tagName === 'LI') {
        event.target.remove();
        console.log('Eliminado del listado')
    }}
