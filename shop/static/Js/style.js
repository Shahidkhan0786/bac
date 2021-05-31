
////product-detail
//$(document).ready(function () {
//  // MDB Lightbox Init
//  $(function () {
//    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
//
//  });
//});











$('.show1').zoomImage();


$('.show-small-img:first-of-type').css({'border': 'solid 1px #951b25', 'padding': '2px'})
$('.show-small-img:first-of-type').attr('alt', 'now').siblings().removeAttr('alt')
$('.show-small-img').click(function () {
  $('#show-img').attr('src', $(this).attr('src'))
  $('#big-img').attr('src', $(this).attr('src'))
  $(this).attr('alt', 'now').siblings().removeAttr('alt')
  $(this).css({'border': 'solid 1px #951b25', 'padding': '2px'}).siblings().css({'border': 'none', 'padding': '0'})
  if ($('#small-img-roll').children().length > 4) {
    if ($(this).index() >= 3 && $(this).index() < $('#small-img-roll').children().length - 1){
      $('#small-img-roll').css('left', -($(this).index() - 2) * 76 + 'px')
    } else if ($(this).index() == $('#small-img-roll').children().length - 1) {
      $('#small-img-roll').css('left', -($('#small-img-roll').children().length - 4) * 76 + 'px')
    } else {
      $('#small-img-roll').css('left', '0')
    }
  }
})


// /next pre b

$('#next-img').click(function (){
  $('#show-img').attr('src', $(".show-small-img[alt='now']").next().attr('src'))
  $('#big-img').attr('src', $(".show-small-img[alt='now']").next().attr('src'))
  $(".show-small-img[alt='now']").next().css({'border': 'solid 1px #951b25', 'padding': '2px'}).siblings().css({'border': 'none', 'padding': '0'})
  $(".show-small-img[alt='now']").next().attr('alt', 'now').siblings().removeAttr('alt')
  if ($('#small-img-roll').children().length > 4) {
    if ($(".show-small-img[alt='now']").index() >= 3 && $(".show-small-img[alt='now']").index() < $('#small-img-roll').children().length - 1){
      $('#small-img-roll').css('left', -($(".show-small-img[alt='now']").index() - 2) * 76 + 'px')
    } else if ($(".show-small-img[alt='now']").index() == $('#small-img-roll').children().length - 1) {
      $('#small-img-roll').css('left', -($('#small-img-roll').children().length - 4) * 76 + 'px')
    } else {
      $('#small-img-roll').css('left', '0')
    }
  }
})

$('#prev-img').click(function (){
  $('#show-img').attr('src', $(".show-small-img[alt='now']").prev().attr('src'))
  $('#big-img').attr('src', $(".show-small-img[alt='now']").prev().attr('src'))
  $(".show-small-img[alt='now']").prev().css({'border': 'solid 1px #951b25', 'padding': '2px'}).siblings().css({'border': 'none', 'padding': '0'})
  $(".show-small-img[alt='now']").prev().attr('alt', 'now').siblings().removeAttr('alt')
  if ($('#small-img-roll').children().length > 4) {
    if ($(".show-small-img[alt='now']").index() >= 3 && $(".show-small-img[alt='now']").index() < $('#small-img-roll').children().length - 1){
      $('#small-img-roll').css('left', -($(".show-small-img[alt='now']").index() - 2) * 76 + 'px')
    } else if ($(".show-small-img[alt='now']").index() == $('#small-img-roll').children().length - 1) {
      $('#small-img-roll').css('left', -($('#small-img-roll').children().length - 4) * 76 + 'px')
    } else {
      $('#small-img-roll').css('left', '0')
    }
  }
})




$(document).ready(

function(){
$('#c11').click(function(){
console.log($('#c1').val())
})

$('#hhh1').hover(function(){
  $('#hhh').css("visibility","hidden");
},
function(){
$('#hhh').css("visibility","visible");
}
);




},

$('.plus-cart').click(function(){

console.log('plus clicked')
var id= $(this).attr("pid").toString();
var elm= this.parentNode.children[2]
//console.log(id)


$.ajax({
 type:"GET",
 url:"/pluscart",
 data:{prod_id:id},
 success:function(data){
 console.log(data)
 elm.innerText = data.quantity
 document.getElementById("amountx").innerText = data.amount
  document.getElementById("totalx").innerText = data.total
 }

})





}),


$('.minus-cart').click(function(){

console.log('minusclicked')
var id= $(this).attr("pid").toString();
var elm= this.parentNode.children[2]
//console.log(id)


$.ajax({
 type:"GET",
 url:"/minuscart",
 data:{prod_id:id},
 success:function(data){
 console.log(data)
 elm.innerText = data.quantity
 document.getElementById("amountx").innerText = data.amount
  document.getElementById("totalx").innerText = data.total
 }

})





}),


$('.remove-cart').click(function(){

console.log('removeclicked')
var id= $(this).attr("pid").toString();
var elm= this
//console.log(id)


$.ajax({
 type:"GET",
 url:"/removecart",
 data:{prod_id:id},
 success:function(data){
 console.log(data)

 document.getElementById("amountx").innerText = data.amount
  document.getElementById("totalx").innerText = data.total
  elm.parentNode.parentNode.parentNode.parentNode.remove()
 }

})





}),


);