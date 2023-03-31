import koaBodyParser from 'koa-bodyparser'

class BodyParser {
  description () {
    return 'Parses the request body, making `ctx.request.body` available to downstream middleware.'
  }
  middleware () {
    return koaBodyParser()
  }
}

export default BodyParser
