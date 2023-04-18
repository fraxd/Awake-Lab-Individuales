$(document).ready(function () {
    const commentList = $('#comment-list');

    commentList.on('click', 'li', function () {
        $(this).remove();
        console.log('Eliminado de la lista')
    });

    $('form').on('submit', function (event) {
        console.log('Agregado a la lista')
        event.preventDefault();
        const commentInput = $('#comment');
        const comment = commentInput.val().trim();

        if (comment !== '') {
            const li = $('<li>').text(comment);
            commentList.append(li);
            commentInput.val('');
        }
    });
});