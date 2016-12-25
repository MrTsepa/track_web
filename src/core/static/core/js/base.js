$(document).ready(function () {
    var editor = ace.edit("ace-editor");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/python");

    $("#submit-code").click(function () {
        submit_code(1, editor.getValue())
    })
});

function submit_code(task_id, code) {
    $.post('/solutions/create/', {
        task: task_id,
        code: code,
        csrfmiddlewaretoken: Cookies.get("csrftoken")
    })
}