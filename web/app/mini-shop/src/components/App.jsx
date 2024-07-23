import React, { useEffect } from 'react'

const tg = window.Telegram.WebApp

console.log(tg)

export const App = () => {

  useEffect(() => {

    tg.ready()

  }, [])

  return (
    <>
        привет
    </>
  )
}
