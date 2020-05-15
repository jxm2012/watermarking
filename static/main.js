/*
Jewin Mathew:

Here is the javascript functions to select
the images and display them on the webpage

*/



//function created for handling the form's input when user uploads image
const submitHandler = (event) => {
  event.preventDefault();
  fetch(event.target.action, {
    method: "POST",
    body: new FormData(event.target), // event.target is the form
  })
  .then((resp) => resp.blob())
  .then((body) => {
    console.log(body);
    const imgSrc = URL.createObjectURL(body);
    console.log(imgSrc);
    document.querySelector("#outputImg").src = imgSrc;
    document.querySelector("#wmk-form").classList.add("hidden");
    document.querySelector(".output-section").classList.remove("hidden");
  });
};

const tryAnother = () => {
  document.querySelector("#wmk-form").classList.remove("hidden");
  document.querySelector(".output-section").classList.add("hidden");
};

//displays name of the image
const displayName = (ref, id) => {
  const [{ name }] = ref.files;
  document.querySelector(`#${id}`).innerText = name;
}
