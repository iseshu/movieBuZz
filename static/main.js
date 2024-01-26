const dosearch =() => {
    const searchValue = document.getElementById('dosearch').value;
    const searchUrl =window.location.href + 'search?query='+searchValue;
    $.get(searchUrl,function(data){
        let itemTemplate = '';
        data.forEach(element => {
            itemTemplate += `
            <div class="item">
                <a href="${element['_id']}/${element['title'].trim().replace(' ', '-')}">
                    <img height="220" width="165" src="${element['image']['link']}" alt="${element['title']}" srcset="">
                    <p>${element['title']}</p>
                </a>
            </div>
        `;
        });
        document.querySelector('.container').innerHTML = itemTemplate;
    })
}
const gohome =() => {
    window.location.href = '/';
}

const displaySearch = () =>{
    let div = document.getElementById('mdivsearch');
    let divstyle = window.getComputedStyle(div).getPropertyValue('display');
    if (divstyle == 'block'){
        div.style.display = 'none';
        document.querySelector('.material-icons').textContent = 'search';
        window.location.href = window.location.href;
    }
    else{
        div.style.display = 'block';
        document.querySelector('.material-icons').textContent = 'close';
        
    }
}