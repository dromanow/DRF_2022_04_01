import {useParams} from 'react-router-dom'
import React, { useState, useEffect } from 'react'
import axios from 'axios'


const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBookList = () =>  {
    const [books, setBooks] = useState([])
    var {id} = useParams()

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/books/', { params: { author: id } })
            .then(response => {
                let books = response.data
                setBooks(books)
            })
            .catch(error => console.log(error))
    }, [setBooks]);

    return (
        <table>
        <th>
            Title
        </th>
        <th>
            Authors
        </th>
        {books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default AuthorBookList
