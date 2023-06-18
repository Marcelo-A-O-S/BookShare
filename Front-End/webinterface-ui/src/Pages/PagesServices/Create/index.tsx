import React from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from 'react-bootstrap/Row';

import { useState, useContext } from 'react'
import AuthContext from '../../../Context/AuthContext';
import Book from '../../../Models/Book';
import Post from '../../../Models/Post';

function Create() {
    const [ book, setBook ] = useState<Book>({} as Book)
    const { user } = useContext(AuthContext)
    //const book = new Book()
    async function FileChange(e: any){
        const file = e.target.files[0];
        console.log(file);
        setBook(prevBook =>(
            {
                ...prevBook,
                nome: file.name
            }
        ))
        if (file) {
            const reader = new FileReader();

            reader.onloadend = () => {
              const base64Data = reader.result;
              console.log(base64Data); // Aqui você pode usar a base64Data como desejar
              setBook(prevBook =>(
                {
                    ...prevBook,
                    livro: base64Data?.toString()
                }
              ))
            };

            reader.readAsDataURL(file);
            console.log("Teste:",reader)
          }


    }
    async function onSubmitForm(e:any){
        e.preventDefault();
        const post = new Post();
        post.idUsuario = user?.id;
        post.livro.id = book.id;
        post.livro.livro = book.livro;
        post.livro.nome = book.nome;
        post.livro.descricao = book.descricao;
        if (user !== null){
            const response =  await fetch("http://127.0.0.1:5000//SalvarPost", {
            method:"POST",
            headers: {
                Authorization: user.papelAtribuido,
                "Content-Type": "application/json"
              },
            body: JSON.stringify(post),
         })
            const result = await response.json();
            console.log(result)
        }


    }
  return (
    <form onSubmit={onSubmitForm}>
        <div>
            <input type="file"
            accept=".pdf"
            onChange={FileChange} />
        </div>
        <div>
            <label>Description </label>
            <input type="text"
            value={book.descricao}
            onChange={(e) => setBook( prevBook =>(
                {
                    ...prevBook,
                    descricao: e.target.value
                }
            ))} />
        </div>
        <button type='submit'>Publicar</button>
    </form>
  )
}

export default Create;
