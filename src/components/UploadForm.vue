<template>
    <div class = "container">
        <div v-if="response.errors != 'novalue'">
            <ul id="vlist">
                <li v-for="(error, index) in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>
        <div v-if="response.message != 'novalue'">
            {{response.message}}
        </div>
        <form method="POST" enctype="multipart/form-data" id = "uploadForm" @submit.prevent="uploadPhoto" >
            <ul class="formstf">
                <li class="form-field">
                    <label>Description <span class="required">*</span></label>
                    <textarea class="textarea" placeholder="Message" v-model="form.description" id = "desc" name = "description"></textarea>
                </li>

                <li class="form-field">
                    <label>Photo <span class="required">*</span></label>
                    <input type="file" accept="image/*" class="form-control-file" @change="updatePhoto($event.target.files)" id ="photo" name= "photo">
                </li>
            </ul>
            <input id="submit" type="submit" value="submit" @click.prevent="uploadPhoto()"/>
        </form> 
    </div>
</template>

<script>
export default {
    data() {
      return {
          response: {},
          csrf_token: '',
          form:{
              description: '',
              photo: {}
          }
      }        
    },
    created() {
        this.getCsrfToken();
    },
    methods:{
        updatePhoto(files){
            console.log(files[0])
                if (!files.length){
                    console.log("??")
                    return;
                } 
                

                this.form.photo = {
                    name: files[0].name,
                    data: files[0]
                };
            },
        uploadPhoto(){
            let self = this
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            form_data.append('photo',this.form.photo.data)
            fetch("/api/upload", { 
                method : 'POST',
                headers: {
                    'X-CSRFToken': this.csrf_token
                },
                body: form_data
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
            // display a success message
            self.response = data;
            console.log(data);
            })
            .catch(function (error) {
            console.log(error);
            });   
        },
        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response)=> response.json())
            .then((data) =>{
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },
        containskey(obj, key){
            return Object.keys(obj).includes(key)
        }
         
    },
    computed: {
        haserr() {
            return this.containsKey(this.response, 'errors');
        },
        hasmsg() {
            return this.containsKey(this.response, 'errors');
        }
    }
    

    
}
</script>

<style>

</style>