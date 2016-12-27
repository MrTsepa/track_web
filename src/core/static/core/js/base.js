$(document).ready(function () {
    var editor = ace.edit("ace-editor");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/python");

    $("#submit-code").click(function () {
        submitCode($(this).data('task_id'), editor.getValue(), function () {
            location.reload(true);
        })
    });

    $(".run_solution").click(function () {
        runSolution($(this).data('solution_id'));
        updateStatuses();
    });

    $(".edit-solution").click(function () {
        editor.setValue($(this).data('solution_code'))
        $(window).scrollTo($("#ace-editor"), 500)
    });

    window.setInterval(updateStatuses, 3000);
});

function runSolution(id) {
    $.get('/solutions/'+id+'/run/')
}

function updateStatuses() {
    var ids = Array();
    $(".solution_status").each(function () {
        ids.push($(this).data('solution_id'));
    });

    $.getJSON('/solutions/statuses/', {ids: ids.join(',')}, function (resultJson) {
        for(var i in resultJson) {
            $(".solution_status[data-solution_id="+i+"]").html(resultJson[i])
        }
    })
}

function submitCode(task_id, code, callback) {
    $.post('/solutions/create/', {
        task: task_id,
        code: code,
        csrfmiddlewaretoken: Cookies.get("csrftoken")
    });
    callback()
}