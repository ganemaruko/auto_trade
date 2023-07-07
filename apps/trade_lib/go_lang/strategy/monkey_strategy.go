package strategy

import "go_lang/go_lang/order"

type MonkeyStrategy struct {
}

func (s MonkeyStrategy) Propose() ProposeResult {
	return [order.Order{
		100	}, ]

}
