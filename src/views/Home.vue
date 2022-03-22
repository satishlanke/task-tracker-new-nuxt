<template>
    <div v-show="showAddTask">
    <AddTask @add-task='addTask'/>
  </div>
   
  <Tasks 
  @toggle-reminder="toggleReminder"
  :tasks="tasks"
   @delete-task="alertDisplay"
  />
   <!-- <button v-on:click="alertDisplay">Click Me!</button> -->
</template>


<script>
import Tasks from '../components/Tasks.vue'
import AddTask from '../components/AddTask.vue'
import DeleteModal from '../components/DeleteModal.vue'
import axios from 'axios'
import swal from 'sweetalert2';

// import DeleteModal from '../components/DeleteModal.vue'
export default {
    name:'Home',
    components: {
        Tasks,
        AddTask,
        DeleteModal
    },
    props:{

        showAddTask:Boolean,
        

    },
    data() {
        return {
            tasks: [],
            showDeleteModal:false
        }
    },
    methods: {
      alertDisplay(id) {
        // alert(id)
        this.$swal({
          title: 'Are you sure?',
          text: 'Deleting Record',
          type: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes Delete it!',
          cancelButtonText: 'No, Keep it!',
          showCloseButton: true,
          showLoaderOnConfirm: true
        }).then((result) => {
          if(result.value) {
            axios.delete(`http://127.0.0.1:5000/tasks/${id}`).then((res)=>{
              console.log(res)
            })
            this.tasks = this.tasks.filter((task)=>task.id!==id)
            this.$swal('Deleted', 'You successfully deleted this item', 'success')
          } else {
            this.$swal('Cancelled', 'Your item is still intact', 'info')
          }
        })
      },
     
      deleteItem(id){
        alert(id)
         this.tasks = this.tasks.filter((task)=>task.id!==id)

      },
        addTask(task) {
          axios.post('http://localhost:5000/tasks',task).then((res)=>{
      console.log(res)
    })
      this.tasks = [...this.tasks,task]
    },
//     modalOpenClose(){
//  this.showDeleteModal= !this.showDeleteModal
//     },
    // deleteTask(id){
      
    //   if(confirm('Are you Sure'))
    //   this.tasks = this.tasks.filter((task)=>task.id!==id)
    
    // },
    toggleReminder(id){
      // alert(id)
     this.tasks = this.tasks.map((task)=> task.id === id 
     ? {...task,reminder: !task.reminder}: task)
     let params={
       reminder: !this.tasks.filter((item)=>id===item.id).reminder
     }
     axios.put(`http://127.0.0.1:5000/tasks/${id}`,params).then((res)=>{
          console.log(res)
        })
     
    },

       async fetchTasks() {
      await axios.get('http://localhost:5000/tasks').then((response)=>{
      this.tasks=response.data.tasks
      
    })
    
    },
  },
  created() {
   this.fetchTasks()
    // this.tasks =[
    //   {
    //     id:1,
    //     text: 'Doctors Appointment',
    //     day: "MArch 1 st at 2: 30 pm ",
    //     reminder: true 
    //   },
    //   {
    //     id:2,
    //     text: 'School appointment',
    //     day: "dec 1 st at 2: 30 pm ",
    //     reminder: false 
    //   },{
    //     id:3,
    //     text: 'Police Appointment',
    //     day: "MArch 1 st at 2: 30 pm ",
    //     reminder: true 
    //   },{
    //     id:4,
    //     text: 'Parents Appointment',
    //     day: "MArch 1 st at 2: 30 pm ",
    //     reminder: true 
    //   }

    // ]
  }
    
}
</script>