import React, { useEffect } from 'react'
import { userReq } from '../services/user.service'

const tg = window.Telegram.WebApp

console.log(tg)



export const App = () => {

  useEffect(() => {

    tg.ready()

    userReq.sendData({ data: tg.initDataUnsafe }).then()

  }, [])


  

  return (
    <>
        <h2>Привет {tg.initDataUnsafe?.user?.first_name}</h2>


    </>
  )
}
