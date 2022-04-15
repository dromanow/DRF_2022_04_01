import {useParams} from 'react-router-dom'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBookList = ({books}) =>  {
    var {id} = useParams()
    var filteredBooks = books.filter((book) => book.authors.includes(parseInt(id)))

    return (
        <table>
        <th>
            Title
        </th>
        <th>
            Authors
        </th>
        {filteredBooks.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default AuthorBookList
