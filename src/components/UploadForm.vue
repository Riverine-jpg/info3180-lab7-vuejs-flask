<template>
    <div class = "container">
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
          response: null,
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
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            console.log(this.form.photo.data)
            form_data.append('photo',this.form.photo.data)
            for (var key of form_data.entries()){
                console.log(key[0] + ', ' + key[1]);
            }
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
        }
         
    }
    

    
}
</script>

<style>

</style>