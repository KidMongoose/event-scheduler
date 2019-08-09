$(() => {
 $('#signin').on('click', (e) => {
    e.preventDefault();
    $('#register-form form').fadeOut();
    $('#register-form').load('/signin')
  })


})