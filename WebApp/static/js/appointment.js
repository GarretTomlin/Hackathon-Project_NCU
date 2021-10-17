$(document).ready(() => {
    $('.make_appointment').on('click', e => {
        $target = $(e.target);
        const id = $target.attr('data-id');
        $.ajax({
            url: "appointments/book",
            type: "POST",
            dataType: "JSON",
            data: { therapist_id: id },
            statusCode: {
                404: () => { console.log("Failed To Retrieve Page"); }
            },
            success: (results) => { window.location.href = "appointments/" }
        })
    })
});