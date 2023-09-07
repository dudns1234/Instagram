const likeButtons = document.querySelectorAll('i.heart')
// console.log(likeButtons)

likeButtons.forEach((likeButton) => {
    // console.log(likeButton)
    likeButton.addEventListener('click',(event)=>{
        let postId = event.target.dataset.postId
        // console.log(postId)

        likeRequest(event.target, postId) // click시에 발생하는 것이기 때문에 순서에는 문제 없음
    })
})

let likeRequest = async (button, postId) => {
    console.log(button, postId)
    // django 서버에 요청을 보낸다
    let likeURL = `/posts/${postId}/like-async/`
    // console.log(postId)
    let response = await fetch(likeURL) // -> 비동기적으로 동작하니까 데이터가 들어올 때까지 기다려달라 / fetch함수가 요청을 보냄
    let result = await response.json()

    // console.log(result)

    // django 서버의 응답에 따라 좋아요 버튼을 수정한다.
    if (result.status){
        // true => 좋아요가 눌린경우
        button.classList.remove('bi-heart')
        button.classList.add('bi-heart-fill')
        button.style.color = 'red'
        let good_count = document.querySelector(`#good${postId}`)
        good_count.innerHTML = `좋아요 ${result.count}개`           
        // button.innerHTML = result.count 
        // const good = document.getElementById("good")
        // good.innerHTML = `좋아요 ${result.count}개` // innerHTML : 여는 태그와 닫는 태그 사이에 있는 데이터
    } else{
        // false => 좋아요 취소
        button.classList.remove('bi-heart-fill')
        button.classList.add('bi-heart')
        button.style.color = 'white'
        let good_count = document.querySelector(`#good${postId}`)
        good_count.innerHTML = `좋아요 ${result.count}개`
        // button.innerHTML = result.count
        // const good = document.getElementById("good")
        // good.innerHTML = `좋아요 ${result.count}개`
    }
}


const click = document.querySelectorAll('i.chat')
// console.log(click)

click.forEach((click1) => {
    click1.addEventListener('click', (event)=>{
        let postId = event.target.dataset.postId
        console.log(postId)
        // let display = document.getElementById("comment_div").style.display
        let comment_show = document.querySelector(`#comment_div${postId}`)
        // console.log(comment_show) 	
        if(comment_show.style.display ==='none'){
            comment_show.style.display = "";
        }else{ 		
            comment_show.style.display = "none";	
        } 
        })

    })

const commet_click = document.querySelectorAll('p.comment_all')
console.log(commet_click)

commet_click.forEach((commet_click1) => {
    commet_click1.addEventListener('click', (event)=>{
        let postId = event.target.dataset.post_id
        console.log(postId)
        // let display = document.getElementById("comment_div").style.display
        let comment_all = document.querySelector(`#comment${postId}`)
        let comment_show = document.querySelector(`#comment_div${postId}`)
        console.log(comment_all) 
        console.log(comment_show) 
        if(comment_all.style.display ==='show'){
            comment_all.style.display = "none"
            comment_show.style.display = "show"
        }else{ 		
            comment_all.style.display = ""
            comment_show.style.display = "none"
        } 
        })

    })
