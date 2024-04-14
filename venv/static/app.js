const Btn = document.querySelector("body > form > button")
const URLBase ='/api/cupcakes'
const imageV = document.querySelector("body > form > input[type=url]:nth-child(4)")
const ratingV = document.querySelector("body > form > input[type=number]:nth-child(3)")
const sizeV = document.querySelector("body > form > input[type=text]:nth-child(2)")
const flavorV = document.querySelector("body > form > input[type=text]:nth-child(1)")
const UL = document.querySelector("body > ul")







addEventListener("click",AddCompcake)
 

async function delT(e){
    id=e.target.dataset.id
    if(e.target.tagName === 'BUTTON'){
       await axios.delete(`/api/todos/${id}`)
       e.target.parentElement.remove()
        alert('delted')
    }
}


async function AddCompcake(e){
    if(e.target === Btn){
        e.preventDefault()
        await axios.post(URLBase,{
            flavor:`${flavorV.value}`,
            rating:ratingV.value,
            size:sizeV.value,
            image:imageV.value
        })
        newLi=document.createElement("LI")
        newLi.innerHTML=`Flavor: ${flavorV.value}`
        UL.append(newLi)
    }
   
}


