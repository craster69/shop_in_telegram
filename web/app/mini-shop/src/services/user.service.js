import axios from 'axios'

class UserReq{

    async sendData(data){

        await axios.post("http://127.0.0.1:8000/", data)


        console.log('работает')

    }

}

export const userReq = new UserReq

