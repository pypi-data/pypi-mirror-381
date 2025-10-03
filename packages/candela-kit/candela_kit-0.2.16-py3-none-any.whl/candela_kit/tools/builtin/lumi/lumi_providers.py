from typing import Dict

from candela_kit.ignite.intent import IObj
from candela_kit.ignite.intent import intent as ci
from candela_kit.tools.base import BaseTool

LUSID_PROVIDERS = [
    "Lusid.Abor",
    "Lusid.Abor.JELine",
    "Lusid.Abor.TrialBalance",
    "Lusid.AborConfiguration",
    "Lusid.AccountingDiary",
    "Lusid.Allocation",
    "Lusid.Block",
    "Lusid.Calendar",
    "Lusid.Calendar.Date",
    "Lusid.ChartOfAccounts",
    "Lusid.ChartOfAccounts.Account",
    "Lusid.CleardownModule",
    "Lusid.CleardownModule.Rule",
    "Lusid.ComplianceRule",
    "Lusid.ComplianceRuleResult",
    "Lusid.CorporateAction",
    "Lusid.CorporateAction.Source",
    "Lusid.CounterpartyAgreement",
    "Lusid.CutLabel",
    "Lusid.DataType",
    "Lusid.Execution",
    "Lusid.FeeRule",
    "Lusid.FeeType",
    "Lusid.Fund",
    "Lusid.Fund.Fee",
    "Lusid.Fund.ValuationPoint",
    "Lusid.Fund.ValuationPointData",
    "Lusid.Fund.ValuationPointData.Breakdown",
    "Lusid.Fund.ValuationPointData.Fee",
    "Lusid.Fund.ValuationPointData.ShareClass",
    "Lusid.Fund.ValuationPointData.ShareClass.Breakdown",
    "Lusid.Fund.ValuationPointJournalEntryLines",
    "Lusid.Fund.ValuationPointPnLSummary",
    "Lusid.Fund.ValuationPointTransactions",
    "Lusid.Fund.ValuationPointTrialBalance",
    "Lusid.FundConfiguration",
    "Lusid.GeneralLedgerProfile",
    "Lusid.GeneralLedgerProfile.Mapping",
    "Lusid.Instrument",
    "Lusid.Instrument.Bond",
    "Lusid.Instrument.CapFloor",
    "Lusid.Instrument.CdsIndex",
    "Lusid.Instrument.ComplexBond",
    "Lusid.Instrument.ContractForDifference",
    "Lusid.Instrument.CreditDefaultSwap",
    "Lusid.Instrument.Equity",
    "Lusid.Instrument.EquityOption",
    "Lusid.Instrument.EquitySwap",
    "Lusid.Instrument.ExchangeTradedOption",
    "Lusid.Instrument.FlexibleLoan",
    "Lusid.Instrument.ForwardRateAgreement",
    "Lusid.Instrument.FundingLeg",
    "Lusid.Instrument.FundShareClass",
    "Lusid.Instrument.Future",
    "Lusid.Instrument.FxForward",
    "Lusid.Instrument.FxOption",
    "Lusid.Instrument.FxSwap",
    "Lusid.Instrument.InflationLeg",
    "Lusid.Instrument.InflationLinkedBond",
    "Lusid.Instrument.InflationSwap",
    "Lusid.Instrument.InterestRateSwap",
    "Lusid.Instrument.InterestRateSwaption",
    "Lusid.Instrument.LoanFacility",
    "Lusid.Instrument.Property",
    "Lusid.Instrument.Quote",
    "Lusid.Instrument.Repo",
    "Lusid.Instrument.SimpleCashFlowLoan",
    "Lusid.Instrument.SimpleInstrument",
    "Lusid.Instrument.TermDeposit",
    "Lusid.Instrument.TotalReturnSwap",
    "Lusid.InstrumentEvent",
    "Lusid.InstrumentEvent.AccumulationEvent",
    "Lusid.InstrumentEvent.BondCouponEvent",
    "Lusid.InstrumentEvent.BondDefaultEvent",
    "Lusid.InstrumentEvent.BondPrincipalEvent",
    "Lusid.InstrumentEvent.CapitalDistributionEvent",
    "Lusid.InstrumentEvent.CashDividendEvent",
    "Lusid.InstrumentEvent.DividendOptionEvent",
    "Lusid.InstrumentEvent.DividendReinvestmentEvent",
    "Lusid.InstrumentEvent.ExpiryEvent",
    "Lusid.InstrumentEvent.FutureExpiryEvent",
    "Lusid.InstrumentEvent.FxForwardSettlementEvent",
    "Lusid.InstrumentEvent.MaturityEvent",
    "Lusid.InstrumentEvent.MbsCouponEvent",
    "Lusid.InstrumentEvent.MbsInterestDeferralEvent",
    "Lusid.InstrumentEvent.MbsInterestShortfallEvent",
    "Lusid.InstrumentEvent.MbsPrincipalEvent",
    "Lusid.InstrumentEvent.MbsPrincipalWriteOffEvent",
    "Lusid.InstrumentEvent.MergerEvent",
    "Lusid.InstrumentEvent.RepoCashFlowEvent",
    "Lusid.InstrumentEvent.RepoPartialClosureEvent",
    "Lusid.InstrumentEvent.ReverseStockSplitEvent",
    "Lusid.InstrumentEvent.ScripDividendEvent",
    "Lusid.InstrumentEvent.SpinOffEvent",
    "Lusid.InstrumentEvent.StockDividendEvent",
    "Lusid.InstrumentEvent.StockSplitEvent",
    "Lusid.InstrumentEvent.SwapCashFlowEvent",
    "Lusid.InstrumentEvent.SwapPrincipalEvent",
    "Lusid.InternalCachedEntityMetadata",
    "Lusid.InternalEventMetadata",
    "Lusid.InternalMovementStoreMetadata",
    "Lusid.LegalEntity",
    "Lusid.LegalEntity.Macroeconomicdata",
    "Lusid.OrderGraphBlock",
    "Lusid.OrderInstruction",
    "Lusid.Participation",
    "Lusid.Person",
    "Lusid.Person.Wealthmanagement",
    "Lusid.PlaceBlocks",
    "Lusid.Placement",
    "Lusid.Portfolio",
    "Lusid.Portfolio.AggregatedReturn",
    "Lusid.Portfolio.AtoB",
    "Lusid.Portfolio.BucketedCashFlow",
    "Lusid.Portfolio.CashLadder",
    "Lusid.Portfolio.Change",
    "Lusid.Portfolio.Constituent",
    "Lusid.Portfolio.CustodianAccount",
    "Lusid.Portfolio.Holding",
    "Lusid.Portfolio.Holding.Property",
    "Lusid.Portfolio.Reconciliation.Generic",
    "Lusid.Portfolio.Reconciliation.Txn",
    "Lusid.Portfolio.Return",
    "Lusid.Portfolio.Txn",
    "Lusid.Portfolio.Txn.Forgui",
    "Lusid.Portfolio.Txn.HoldingContributor",
    "Lusid.Portfolio.Txn.HoldingContributor.Forgui",
    "Lusid.Portfolio.Txn.HoldingContributor.Yield",
    "Lusid.Portfolio.Txn.Output",
    "Lusid.Portfolio.Txn.Output.Forgui",
    "Lusid.Portfolio.Txn.Output.Yield",
    "Lusid.Portfolio.Txn.Property",
    "Lusid.Portfolio.Txn.Yield",
    "Lusid.Portfolio.Valuation",
    "Lusid.Portfolio.Valuation.Measure",
    "Lusid.PortfolioGroup",
    "Lusid.PortfolioOrder",
    "Lusid.PostingModule",
    "Lusid.PostingModule.Rule",
    "Lusid.Property",
    "Lusid.Property.Definition",
    "Lusid.ReferenceList",
    "Lusid.Relationship",
    "Lusid.Relationship.Definition",
    "Lusid.RunCompliance",
    "Lusid.Scope",
    "Lusid.Sequence",
    "Lusid.StagedModification",
    "Lusid.StagedModification.RequestedChange",
    "Lusid.StagingRuleSet",
    "Lusid.StagingRuleSet.StagingRule",
    "Lusid.TransactionType",
    "Lusid.TransactionType.SideDefinition",
    "Lusid.TransferAgency.OrderDates",
    "Lusid.UnitResult.StructuredResult",
    "Lusid.Valuation.Recipe",
]


# noinspection SqlNoDataSourceInspection
class GetLumiProviders(BaseTool):
    def intent(self) -> IObj:
        apps = ["lusid", "luminesce"]
        return ci.obj(
            provider=ci.enum(*LUSID_PROVIDERS),
            provider_type=ci.enum(*apps),
        )

    def apply(self, intent: Dict) -> Dict:
        provider_pattern = intent.get("provider")

        entity_filter = f"[TableName] == '{provider_pattern}'"

        sql = f"""SELECT
   [TableName] AS [TableName], [FieldName] AS [ColumnName], [Description] AS [ColumnDescription]
FROM
   [Sys.Field]
WHERE
   [FieldType] = 'Column'
   AND {entity_filter}
   AND [IsMain]
"""
        self.push_wait_msg(f"Running SQL:\n{sql}")
        df = self.lumipy_client().run(sql, quiet=True).fillna("N/A")

        table_name = df["TableName"].iloc[0]
        columns = []
        for _, row in df.iterrows():
            columns.append(
                {
                    "name": row.ColumnName,
                    "description": row.ColumnDescription,
                }
            )
        return {"table": table_name, "columns": columns}
