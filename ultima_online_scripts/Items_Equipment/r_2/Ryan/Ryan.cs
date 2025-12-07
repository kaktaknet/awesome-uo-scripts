using System;
using Server;
using Server.Items;
using EDI = Server.Mobiles.EscortDestinationInfo;

namespace Server.Mobiles
{
	public class Ryan : BaseRyan
	{
		[Constructable]
		public Ryan()
		{
			Title = "The Man Whore";

			//SetSkill( SkillName.Parry, 80.0, 100.0 );
			//SetSkill( SkillName.Swords, 80.0, 100.0 );
			//SetSkill( SkillName.Tactics, 80.0, 100.0 );
		}

		public override bool CanTeach{ get{ return false; } }
		public override bool ClickTitle{ get{ return true; } } // Do not display 'the noble' when single-clicking
		
		
		private static int GetRandomHue()
		{
			switch ( Utility.Random( 6 ) )
			{
				default:
				case 0: return 0;
				case 1: return Utility.RandomBlueHue();
				case 2: return Utility.RandomGreenHue();
				case 3: return Utility.RandomRedHue();
				case 4: return Utility.RandomYellowHue();
				case 5: return Utility.RandomNeutralHue();
			}
		}

		public override void InitOutfit()
		{
			AddItem( new FancyShirt() );

			int lowHue = GetRandomHue();

			AddItem( new LongPants( lowHue ) );

 			AddItem( new ThighBoots( lowHue ) );

			switch ( Utility.Random( 2 ) )
			{
				case 0: AddItem( new ShortHair( Utility.RandomHairHue() ) ); break;
				case 1: AddItem( new ReceedingHair( Utility.RandomHairHue() ) ); break;
				
			}

			PackGold( 700, 800 );
		}

		public Ryan ( Serial serial ) : base( serial )
		{
			
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}