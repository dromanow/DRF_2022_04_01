const BookItem = ({book, authors, deleteBook}) => {
    let authorsStr = book.authors.map(authorId => authors.find(a => a.id == authorId ).last_name)

    return (
        <tr>
            <td>{book.title}</td>
            <td>{book.authors.map(authorId => authors.find(a => a.id == authorId).last_name) }</td>
            <td><button onClick={()=>deleteBook(book.id)} >Delete</button></td>
        </tr>
    )
}

const BookList = ({books, authors, deleteBook}) =>  {
    return (
        <table>
        <th>
            Title
        </th>
        <th>
            Authors
        </th>
        {books.map((book) => <BookItem book={book} authors={authors} deleteBook={deleteBook} />)}
        </table>
    )
}

export default BookList
