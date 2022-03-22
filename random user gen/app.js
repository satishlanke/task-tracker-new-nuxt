const app = Vue.createApp(
    {
        
        data() {
            return {
                firstName:'John',
                lastName:'Lanke',
                email:'satishlanke31@gmail.com',
                phone:'0123456788',
                gender:'male',
                picture:'https://vueschool.io/media/818121f696debe28debfb265f8dc4c16/vuejs-3-master-class-transparent.png'
            }
        }, 
        methods:{
            async getUser() {
                const res = await fetch('https://randomuser.me/api')
                const {results} = await res.json()
                results.map((results)=>{
                    this.firstName=results.name.first
                this.lastName=results.name.last
                this.email=results.email
                this.phone=results.phone
                this.gender=results.gender
                this.picture=results.picture.large

                })
                console.log(results)
                
            }
        }
    }
)
app.mount('#app')