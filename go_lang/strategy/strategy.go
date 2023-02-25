package strategy

import (
	"go_lang/go_lang/order"
)

// 未確定なのでtypeで抽象化しておきます(果たして意味があるのか...)
type ProposeResult = []order.Order

type Strategist interface {
	Propose() ProposeResult
}
