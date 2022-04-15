const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BookList = ({books}) =>  {
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

export default BookList
