<template>
  <div v-if="myModel">
    <transition name="model">
     <div class="modal-mask">
      <div class="modal-wrapper">
       <div class="modal-dialog">
        <div class="modal-content">
         <div class="modal-header">
          <button type="button" class="close" @click="$emit('modal-open-close')"><span aria-hidden="true">&times;</span></button>
       
         </div>
         <div class="modal-body">
          
          <h5>Are you want to proceed</h5>
          <div align="center">
           <input type="hidden" v-model="hiddenId" />
           <button @click="$emit('deleteItem',task.id)" class="btn-danger">Delete</button>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </transition>
   </div>
</template>

<script>
import Button from './Button.vue'
export default {
  components: { Button },
  name: 'DeleteModal',
  props:{
    myModel:Boolean
  }
 

    
}
</script>

 <style>
   .modal-mask {
     position: fixed;
     z-index: 9998;
     top: 0;
     left: 0;
     width: 100%;
     height: 100%;
     background-color: rgba(0, 0, 0, .5);
     display: table;
     transition: opacity .3s ease;
   }

   .modal-wrapper {
     display: table-cell;
     vertical-align: middle;
   }
  </style>