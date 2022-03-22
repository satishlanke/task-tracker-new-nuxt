<template>
    <div v-for="task in tasks"  :key="task.id" >
       <Task
       @toggle-reminder="$emit('toggle-reminder',task.id) "
     @delete-task="$emit('delete-task',task.id)"
      
        :task="task"/>
        <!-- <DeleteModal @modal-open-close="$emit('modal-open-close')" @deleteItem="$emit('deleteItem',task.id)"/> -->
    </div>
</template>



<script>
import DeleteModal from './DeleteModal.vue'
import Task from './Task.vue'
export default {
    name: 'Tasks',
    props:{
        tasks : Array
    },
    components:{
        Task,DeleteModal
    },
    emits: ['delete-task','toggle-reminder']
}
</script>