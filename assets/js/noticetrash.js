const noticeTrashes = document.querySelectorAll("#jsNoticeTrash");

function deleteNotice(id) {
    const link = document.createElement("a");
    let href = window.location.href
    let hreflist = href.split("users")
    console.log(hreflist[0])
    link.href = hreflist[0] + `notices/${id}/delete?next=${href}`
    console.log(link.href)
    document.body.appendChild(link);
    link.click();
}

function handleNoticeTrash() {
    let id = this.querySelector("span").textContent;
    console.log(id)
    let result = confirm("공지를 삭제하시겠습니까?")
    console.log(result)
    if (result) {
        deleteNotice(id)

    }
}
// {% url 'notices:delete' notice.pk %}?next = {{ request.path }}
// path("/notices/<int:pk>/delete", views.delete_notice, name = "delete"),



function init() {
    console.log("listenling")
    noticeTrashes.forEach(noticeTrash => {
        noticeTrash.addEventListener("click", handleNoticeTrash)
    });
}

if (noticeTrashes) {
    init()
}